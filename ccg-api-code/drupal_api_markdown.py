# Imports
import os
import re
import sys
import requests
import time
import json
from pathlib import Path
from markdownify import markdownify as md
from bs4 import BeautifulSoup

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

# Cache management
CACHE_FILE = os.path.join(os.path.dirname(__file__), "api_cache.json")
use_cache = False

def save_to_cache(criterion, web_data):
    """Save web data to cache file"""
    cache_data = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cache_data = json.load(f)
    
    cache_data[criterion] = web_data
    
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache_data, f, indent=2)
    print(f"Cached data for {criterion}")

def load_from_cache(criterion):
    """Load web data from cache file"""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cache_data = json.load(f)
        if criterion in cache_data:
            print(f"Using cached data for {criterion}")
            return cache_data[criterion]
    return None

def gather_data_from_web(criterion):
    web_data = {}

    base_url = "https://healthit.gov"

    headers = {'User-Agent': os.environ.get('MY_USER_AGENT')}
    
    if use_cache:
        cached_responses = load_from_cache(criterion)
        if cached_responses:
            entity_ids_json = cached_responses["entity_ids"]
            raw_responses = cached_responses["responses"]
        else:
            return {}
    else:
        entity_ids_json = requests.get(f"{base_url}/{criterion}?_format=json", headers=headers).json()["field_clarification_table"]
        raw_responses = {}

    data_url = "https://healthit.gov/entity/paragraph"

    for entity_id in entity_ids_json:
        request_url = "{}/{}?_format=json".format(data_url, entity_id["target_id"])

        if use_cache:
            data_json = raw_responses[str(entity_id["target_id"])]
        else:
            data_json = requests.get(request_url, headers=headers).json()
            raw_responses[str(entity_id["target_id"])] = data_json
            time.sleep(1.2) # Buffer between API calls for 50 calls / minute

        element = data_json["field_standard_s_referenced"][0]["processed"]
        
        if not use_cache:
            soup_temp = BeautifulSoup(element, 'html.parser')
            element_temp = soup_temp.get_text()
            element_temp = strip_non_alphanumeric(element_temp)
            print("\tGET {} for {}".format(request_url, element_temp))
        
        soup = BeautifulSoup(element, 'html.parser')
        element = soup.get_text()

        element = strip_non_alphanumeric(element)
        data = data_json["field_technical_explanations_and"][0]["processed"]

        web_data[element] = data

    # Save raw API responses to cache
    if not use_cache:
        save_to_cache(criterion, {"entity_ids": entity_ids_json, "responses": raw_responses})
    
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

    while pointer < len(onc_template_str) and onc_template_str[pointer] == "\t":
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

    web_data = gather_data_from_web(criterion_endpoint)

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

        clarifications_list = ""
        clarifications_list = md(referenced_paragraph_data)
        clarifications_list = clarifications_list.lstrip('\n') # Remove leading new lines
        
        if tabbed:
            clarifications_list_by_line = md(referenced_paragraph_data).lstrip('\n').split("\n")
            # clarifications_list_by_line = list(filter(None, clarifications_list_by_line)) # Remove empty strings (Not sure I should actually try and clean the API output here where focus is better spent cleaning the API itself)
            clarifications_list_by_line = list(map(lambda x: "\t" + x, clarifications_list_by_line)) # Add tabs to each line
            clarifications_list = '\n'.join(clarifications_list_by_line)

        _, pointer = read_to_line_end(onc_template_str, onc_template_str.find(tag))

        to_be_replaced_beginning, to_be_replaced_end = get_existing_clarification_text(onc_template_str, pointer + 1)

        onc_template_str = onc_template_str[:to_be_replaced_beginning] + clarifications_list + onc_template_str[to_be_replaced_end:]
    
    write_processed_doc(onc_template_str, file_path)

def main():
    global use_cache
    
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    
    # Check for cache flag
    if "--cache" in opts:
        use_cache = True
        opts.remove("--cache")
        print("Using cached data")

    params = zip(opts, args)

    os.chdir("docs")
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

    for path, subdir, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[-1].lower() # grab the file extension
            if ext == ".md":
                file_path = os.path.join(path, file)

                onc_template = open(file_path, 'r', encoding="utf8")
                onc_template_str = onc_template.read() 
                print("Processing {}...".format(file_path))  
                process_template(onc_template_str, file_path)

    print("All processing complete!")

if __name__ == "__main__":
    main()