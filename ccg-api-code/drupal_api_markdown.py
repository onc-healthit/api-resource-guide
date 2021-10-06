# Imports
import os
import re
import sys
import requests
import json
import time
from pathlib import Path
from bs4 import BeautifulSoup

call_api = True

def read_to_line_end(input_str, pos):
    """Builds a string from a position to the end of the line
    and returns the result.

    Parameters
    ----------
    input_str : str, required
        String containing template file contents (default is None)

    pos : int, required
        Integer represetning the position in the input_str we start
        reading at and continue to first new line.
    """
    pointer = pos
    c = input_str[pointer]

    while c != "\n":
        pointer += 1

        # End of file check
        if pointer >= len(input_str):
            break   

        c = input_str[pointer]

    return input_str[pos:pointer], pointer

def strip_non_alphanumeric(data):
    p = re.compile(r'\W+')
    return p.sub('', data).strip()

def resolve_li_links(md_str, links_soup):
    for link in links_soup:
        link["target"] = "_blank"
        link_text = link.get_text()
        link_html = str(link)
        md_str = md_str.replace(link_text, link_html)

    return md_str

def html_list_to_markdown(input, prefix = ""):
    li_tags = input.find("ul").contents

    output = ""

    for li_tag in li_tags:
        nested_list = li_tag.find("ul")

        if nested_list == -1:
            continue

        if nested_list == None:
            links = li_tag.find_all('a')

            li_tag_str = li_tag.get_text()

            if links:
                li_tag_str = resolve_li_links(li_tag_str, links)

            output = output + "{}- ".format(prefix) + li_tag_str.strip() + "\n"
        else:
            # Hacking a  deep copy of li_tag
            li_tag_copy = str(li_tag)
            li_tag_copy = BeautifulSoup(li_tag_copy, 'html.parser')

            li_tag_copy.find("ul").decompose()
            text = li_tag_copy.get_text()

            links = li_tag_copy.find_all('a')
            if links:
                text = resolve_li_links(text, links)

            output = output + "{}- {}\n".format(prefix, text.strip()) + html_list_to_markdown(li_tag, prefix + "\t")       

    return output

def gather_data_from_web(criterion):
    web_data = {}

    base_url = "https://healthit.gov"

    entity_ids_json = None
    if call_api:
        entity_ids_json = requests.get("{}/{}?_format=json".format(base_url, criterion)).json()["field_clarification_table"]
    else:
        with open('cached_entities.json') as f:
            entity_ids_json = json.load(f)["field_clarification_table"]

    data_url = "https://healthit.gov/entity/paragraph"

    for entity_id in entity_ids_json:
        data_json = None
        if call_api:
            data_json = requests.get("{}/{}?_format=json".format(data_url, entity_id["target_id"])).json()
            time.sleep(1.2) # Buffer between API calls for 50 calls / minute
        else:
            with open('cached_test_files/cached_response.json') as f:
                data_json = json.load(f)

        element = data_json["field_standard_s_referenced"][0]["processed"]
        
        soup = BeautifulSoup(element, 'html.parser')
        element = soup.get_text()

        element = strip_non_alphanumeric(element)
        data = data_json["field_technical_explanations_and"][0]["processed"]

        web_data[element] = data

    return web_data

def write_processed_doc(output, file_path):
    # Output final result to file
    output_file = open(file_path, 'w', encoding='utf-8')
    output_file.write(output)
    output_file.close()

    print("Processed file exported to: {}".format(file_path))

def get_existing_clarification_text(onc_template_str, pointer):
    _, pointer = read_to_line_end(onc_template_str, pointer)
    pointer = pointer + 1 # Move past new line

    beginning_pointer = pointer

    while onc_template_str[pointer] == "\t":
        _, pointer = read_to_line_end(onc_template_str, pointer)
        pointer = pointer + 1 # Move past new line

    return beginning_pointer, pointer

def process_template(onc_template_str, file_path):
    # Search for the criterion endpoint path
    criterion_endpoint_tag = re.findall(r'\$criterion-endpoint\{\"(.*?)\"\}', onc_template_str)

    # If no endpoint tag is found, return
    if not criterion_endpoint_tag:
        print("INFO: No $criterion-endpoint{...} defined in %s. Skipping file." % file_path)
        return

    criterion_endpoint = criterion_endpoint_tag[0] # Extracting criterion endpoint value

    web_data = None
    if call_api:
        api_check = input("Warning! Numerous API calls are about to be made, are you sure you want to proceed? ('y' for yes): ")
        if api_check.lower() == 'y':
            web_data = gather_data_from_web(criterion_endpoint)
        else:
            print("Exiting...")
            exit()
    else:
        with open('cached_test_files/g8-cache.json') as f:
            web_data = json.load(f)

    # Extracting list of $ref tags
    tags = re.findall(r'\$ref\{.*?\}', onc_template_str)

    # Loop through each tag
    for tag in tags:
        function_line_striped = ""

        # Strip non alphanumeric characters out of content between quotes
        in_quotes = re.findall('"([^"]*)"', tag) # Extracting data between quotes
        for quote in in_quotes:
            striped_quote = strip_non_alphanumeric(quote)
            tag_striped = tag.replace(quote, striped_quote)

        referenced_parameters = re.findall(r'\{(.*?)\}', tag_striped)[0].split(",") # Extracting parameters
        referenced_paragraph_key = re.findall('"([^"]*)"', referenced_parameters[0])[0] # Extracting paragraph key
        referenced_paragraph_key = strip_non_alphanumeric(referenced_paragraph_key)

        # Checking for tabbed parameter
        tabbed = False
        if len(referenced_parameters) > 1:
            parameter = referenced_parameters[1].strip()
            if parameter == "tabbed":
                tabbed = True

        referenced_paragraph_data = web_data[referenced_paragraph_key]

        soup = BeautifulSoup(referenced_paragraph_data, 'html.parser')

        clarifications_list = ""
        if tabbed:
            clarifications_list = html_list_to_markdown(soup, "\t")
        else:
            clarifications_list = html_list_to_markdown(soup)

        _, pointer = read_to_line_end(onc_template_str, onc_template_str.find(tag))

        to_be_replaced_beginning, to_be_replaced_end = get_existing_clarification_text(onc_template_str, pointer + 1)

        onc_template_str = onc_template_str[:to_be_replaced_beginning] + clarifications_list + onc_template_str[to_be_replaced_end:]
    
    write_processed_doc(onc_template_str, file_path)

def main():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    params = zip(opts, args)

    os.chdir("../docs")
    directory = os.getcwd()

    for (flag, value) in params:
        # -i is "input" -- means specific file has been specified 
        if flag == "-i":
            onc_template = open("{}/{}".format(directory,  value), 'r', encoding="utf8")
            onc_template_str = onc_template.read()
            onc_template.close()
            process_template(onc_template_str, value)
            print("All processing complete!")
            exit()

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext == ".md":
                onc_template = open(file, 'r', encoding="utf8")
                onc_template_str = onc_template.read() 
                file_path = Path(directory) / file 
                print("Processing {}...".format(file_path))  
                process_template(onc_template_str, file_path)

    print("All processing complete!")

if __name__ == "__main__":
    main()