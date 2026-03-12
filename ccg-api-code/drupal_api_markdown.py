# Imports
import difflib
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md


HTML_CACHE_ROOT = Path("/tmp/healthit-ccg-cache")
BASE_URL = "https://healthit.gov"
HTML_ENDPOINT_MAP = {
    "test-method/standardized-api-patient-and-population-services":
        "test-method/standardized-api-for-patient-and-population-services-acb-atl/",
    "condition-ccg/application-programming-interfaces":
        "certification-health-it/conditions-ccg/application-programming-interfaces/",
}
use_cache = False
_html_cache = {}


def read_to_line_end(input_str, pos):
    """Build a string from a position to the end of the line."""
    pointer = pos
    c = input_str[pointer]

    while c != "\n":
        pointer += 1

        if pointer >= len(input_str):
            break

        c = input_str[pointer]

    return input_str[pos:pointer], pointer


def strip_non_alphanumeric(data):
    p = re.compile(r"\W+")
    return p.sub("", data).strip()


PARSED_KEY_ALIASES = {
    strip_non_alphanumeric(
        "Paragraph (g)(10)(v)(B) Authentication and authorization – Authentication and authorization for system scopes"
    ): strip_non_alphanumeric("Paragraph (g)(10)(v)(B) Authentication and authorization for system scopes"),
}


def write_processed_doc(output, file_path):
    output_file = open(file_path, "w", encoding="utf-8")
    output_file.write(output)
    output_file.close()

    print("Processed file exported to: {}".format(file_path))


def get_existing_clarification_text(onc_template_str, pointer):
    _, pointer = read_to_line_end(onc_template_str, pointer)
    pointer = pointer + 1

    beginning_pointer = pointer

    while pointer < len(onc_template_str) and onc_template_str[pointer] == "\t":
        _, pointer = read_to_line_end(onc_template_str, pointer)
        pointer = pointer + 1

    return beginning_pointer, pointer


def normalize_content_for_comparison(content):
    content = content.replace("\r\n", "\n").replace("\r", "\n").replace("\xa0", " ")

    lines = content.split("\n")
    normalized_lines = []

    for line in lines:
        s = line.lstrip(" \t")
        s = re.sub(r"^([*+\-])\s+", "- ", s)
        s = re.sub(r"\s+", " ", s).strip()

        if s:
            normalized_lines.append(s)

    return "\n".join(normalized_lines)


def preserve_existing_formatting(existing_content, new_content, tabbed):
    existing_normalized = normalize_content_for_comparison(existing_content)
    new_normalized = normalize_content_for_comparison(new_content)

    if existing_normalized == new_normalized:
        return existing_content

    def norm_line(s):
        s = s.replace("\r\n", "\n").replace("\r", "\n").replace("\xa0", " ")
        s = s.lstrip(" \t")
        s = re.sub(r"^([*+\-])\s+", "- ", s)
        s = re.sub(r"\s+", " ", s).strip()
        return s

    existing_lines = existing_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)
    existing_norm = [norm_line(l) for l in existing_lines]
    new_norm = [norm_line(l) for l in new_lines]

    sm = difflib.SequenceMatcher(a=existing_norm, b=new_norm)
    merged_lines = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            merged_lines.extend(existing_lines[i1:i2])
        else:
            merged_lines.extend(new_lines[j1:j2])

    merged = "".join(merged_lines)

    if normalize_content_for_comparison(merged) == new_normalized:
        return merged

    last_nonwhite_pos = -1
    for i in range(len(existing_content) - 1, -1, -1):
        if existing_content[i] not in " \t\n\r":
            last_nonwhite_pos = i
            break

    if last_nonwhite_pos >= 0:
        trailing_whitespace = existing_content[last_nonwhite_pos + 1:]
        new_last_nonwhite_pos = -1
        for i in range(len(new_content) - 1, -1, -1):
            if new_content[i] not in " \t\n\r":
                new_last_nonwhite_pos = i
                break
        if new_last_nonwhite_pos >= 0:
            new_content_meaningful = new_content[:new_last_nonwhite_pos + 1]
            return new_content_meaningful + trailing_whitespace

    return new_content


def resolve_endpoint(criterion):
    resolved = HTML_ENDPOINT_MAP.get(criterion, criterion)
    return resolved.strip("/")


def cache_path_for_endpoint(endpoint):
    digest = hashlib.sha256(endpoint.encode("utf-8")).hexdigest()[:12]
    filename = endpoint.strip("/").replace("/", "-")
    filename = re.sub(r"[^A-Za-z0-9._-]+", "-", filename)
    return HTML_CACHE_ROOT / f"{filename}-{digest}.html"


def fetch_html(endpoint):
    endpoint = resolve_endpoint(endpoint)
    cache_path = cache_path_for_endpoint(endpoint)

    if endpoint in _html_cache:
        return _html_cache[endpoint]

    if use_cache and cache_path.exists():
        html = cache_path.read_text(encoding="utf-8")
        _html_cache[endpoint] = html
        print(f"Using cached HTML for {endpoint}")
        return html

    url = f"{BASE_URL}/{endpoint}/"
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Fetching {url}")
    subprocess.run(
        ["curl", "-L", url, "-o", str(cache_path)],
        check=True,
        env=os.environ.copy(),
    )

    html = cache_path.read_text(encoding="utf-8")
    _html_cache[endpoint] = html
    print(f"Saved HTML cache to {cache_path}")
    return html


def inner_html(element):
    return "".join(str(child) for child in element.contents).strip()


def parse_g10_clarifications(soup):
    web_data = {}
    root = soup.select_one("div.clarifications-content[data-block='clarifications']")
    if not root:
        raise ValueError("Could not find (g)(10) clarifications container in HTML")

    buttons = root.select("button.usa-accordion__button")
    for button in buttons:
        content_id = button.get("aria-controls")
        if not content_id:
            continue

        content = root.select_one(f"div#{content_id}")
        if not content:
            continue

        section_content = content.select_one("div.section-content")
        if not section_content:
            continue

        heading_text = " ".join(button.stripped_strings)
        heading_text = re.sub(r"\s+", " ", heading_text).strip()

        if heading_text == "Applies to Entire Criterion":
            key = heading_text
        else:
            code = button.get("data-version", "").strip()
            if not code:
                raise ValueError(f"Missing data-version on g10 accordion heading: {heading_text}")
            key = f"{code} {heading_text.replace(code, '', 1).strip()}"

        web_data[strip_non_alphanumeric(key)] = inner_html(section_content)

    if not web_data:
        raise ValueError("No (g)(10) clarification sections were parsed from HTML")

    return web_data


def parse_404_clarifications(soup):
    web_data = {}
    heading = soup.find(id="h-condition-explanations-and-clarifications")
    if not heading:
        raise ValueError("Could not find 404 clarifications heading in HTML")

    accordion = heading.find_next("div", class_="wp-block-uswds-gutenberg-uswds-accordion")
    if not accordion:
        raise ValueError("Could not find 404 clarifications accordion in HTML")

    for item in accordion.select("div.wp-block-uswds-gutenberg-uswds-accordion-item"):
        button = item.select_one("button.usa-accordion__button")
        content = item.select_one("div.usa-accordion__content")
        if not button or not content:
            continue

        key = strip_non_alphanumeric(" ".join(button.stripped_strings))
        web_data[key] = inner_html(content)

    if not web_data:
        raise ValueError("No 404 clarification sections were parsed from HTML")

    return web_data


def gather_data_from_web(criterion):
    html = fetch_html(criterion)
    soup = BeautifulSoup(html, "html.parser")
    resolved = resolve_endpoint(criterion)

    if "standardized-api-for-patient-and-population-services-acb-atl" in resolved:
        return parse_g10_clarifications(soup)

    if "application-programming-interfaces" in resolved:
        return parse_404_clarifications(soup)

    raise ValueError(f"No HTML parser configured for endpoint: {criterion}")


def process_template(onc_template_str, file_path):
    criterion_endpoint_tag = re.findall(r'\$criterion-endpoint\{\"(.*?)\"\}', onc_template_str)

    if not criterion_endpoint_tag:
        print("INFO: No $criterion-endpoint{...} defined in %s. Skipping file." % file_path)
        return

    criterion_endpoint = criterion_endpoint_tag[0]
    web_data = gather_data_from_web(criterion_endpoint)
    tags = re.findall(r"\$ref\{.*?\}", onc_template_str)

    for tag in tags:
        in_quotes = re.findall('"([^"]*)"', tag)
        tag_striped = tag
        for quote in in_quotes:
            striped_quote = strip_non_alphanumeric(quote)
            tag_striped = tag_striped.replace(quote, striped_quote)

        referenced_parameters = re.findall(r"\{(.*?)\}", tag_striped)[0].split(",")
        referenced_paragraph_key = re.findall('"([^"]*)"', referenced_parameters[0])[0]
        referenced_paragraph_key = strip_non_alphanumeric(referenced_paragraph_key)

        tabbed = False
        if len(referenced_parameters) > 1:
            parameter = referenced_parameters[1].strip()
            if parameter == "tabbed":
                tabbed = True

        lookup_key = referenced_paragraph_key
        if lookup_key not in web_data:
            lookup_key = PARSED_KEY_ALIASES.get(referenced_paragraph_key, referenced_paragraph_key)

        if lookup_key not in web_data:
            available = "\n".join(sorted(web_data.keys()))
            raise KeyError(
                f"Could not find parsed clarification section for key: {referenced_paragraph_key}\n"
                f"Available keys:\n{available}"
            )

        referenced_paragraph_data = web_data[lookup_key]
        clarifications_list = md(referenced_paragraph_data).lstrip("\n")

        if tabbed:
            clarifications_list_by_line = md(referenced_paragraph_data).lstrip("\n").split("\n")
            clarifications_list_by_line = list(map(lambda x: "\t" + x, clarifications_list_by_line))
            clarifications_list = "\n".join(clarifications_list_by_line)

        _, pointer = read_to_line_end(onc_template_str, onc_template_str.find(tag))
        to_be_replaced_beginning, to_be_replaced_end = get_existing_clarification_text(
            onc_template_str, pointer + 1
        )

        existing_content = onc_template_str[to_be_replaced_beginning:to_be_replaced_end]
        final_content = preserve_existing_formatting(existing_content, clarifications_list, tabbed)
        onc_template_str = (
            onc_template_str[:to_be_replaced_beginning]
            + final_content
            + onc_template_str[to_be_replaced_end:]
        )

    write_processed_doc(onc_template_str, file_path)


def main():
    global use_cache

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if "--cache" in opts:
        use_cache = True
        opts.remove("--cache")
        print("Using cached HTML when available")

    params = zip(opts, args)

    os.chdir("docs")
    directory = os.getcwd()

    for (flag, value) in params:
        if flag == "-i":
            onc_template = open("{}/{}".format(directory, value), "r", encoding="utf8")
            onc_template_str = onc_template.read()
            onc_template.close()
            process_template(onc_template_str, value)
            print("All processing complete!")
            exit()

    for path, subdir, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext == ".md":
                file_path = os.path.join(path, file)

                onc_template = open(file_path, "r", encoding="utf8")
                onc_template_str = onc_template.read()
                print("Processing {}...".format(file_path))
                process_template(onc_template_str, file_path)

    print("All processing complete!")


if __name__ == "__main__":
    main()
