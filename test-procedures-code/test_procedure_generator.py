import re

# Read in test-procedure file
main_list = open("test-procedure.txt", encoding="utf8")
main_list_text = main_list.read()
main_list.close()

# Match each test procedure step
search_set = re.findall(r'<!--((.|\n)*?)-->', main_list_text)

# Loop through each map and store in dict
test_procedure_steps = {}

for result in search_set:
    unique_id = re.search(r'([A-Z]{3})-([A-Z]{3})-([0-9]+(-\(.*?\))?)', result[0]).group()

    # Remove the -(...) stuff
    step_text = re.sub(r'-\(.*?\)', '', result[0])

    test_procedure_steps[unique_id] = step_text.strip()

# Build test procedure indicies

test_procedure_indicies = [
    {
        "pretty_title": "Base regulatory standards (US Core v3.1.1 + USCDI V1, SMART App Launch v1, Bulk Data v1)",
        "file_name_unique_id": "OIv5O",
        "test_procedure_paragraphs": [
            ("Paragraph (g)(10)(v)(A) - Authentication and authorization for patient and user scopes", ["AUT-PAT-4"])
        ] 
    },
        {
        "pretty_title": "SVAP option (US Core v3.1.1 + USCDI V1, SMART App Launch v2, Bulk Data v1)",
        "file_name_unique_id": "caQqq",
        "test_procedure_paragraphs": [
            ("Paragraph (g)(10)(v)(A) - Authentication and authorization for patient and user scopes", ["AUT-PAT-4", "AUT-PAT-24", "AUT-PAT-25"])
        ] 
    },
        {
        "pretty_title": "SVAP option (US Core v5.0.1 + USCDI V2, SMART App Launch v2, Bulk Data v1)",
        "file_name_unique_id": "jQuzj",
        "test_procedure_paragraphs": [
            ("Paragraph (g)(10)(v)(A) - Authentication and authorization for patient and user scopes", ["AUT-PAT-4", "AUT-PAT-24", "AUT-PAT-25-(US Core 5.0.1)"])
        ] 
    }
]

for test_procedure_index in test_procedure_indicies:
    test_procedure = ""
    # Add title
    test_procedure += "# {}\n\n".format(test_procedure_index["pretty_title"])

    for paragraph in test_procedure_index["test_procedure_paragraphs"]:
        # Add paragraph title
        test_procedure += "## {}\n".format(paragraph[0])

        count = 1
        for step in paragraph[1]:
            # step = re.sub(r'-\(.*\)', '', step)

            test_procedure += "\n{}. {}\n".format(count, test_procedure_steps[step])
            count += 1

    # Write to file
    f = open("../docs/g10-test-procedures/{}.md".format(test_procedure_index["file_name_unique_id"]), "w", encoding='utf-8')
    f.write(test_procedure + "\n--8<-- \"includes/abbreviations.md\"")
    f.close()