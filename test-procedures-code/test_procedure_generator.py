import xml.etree.ElementTree as ET
import itertools

#names of standards with variable combinations
USCORE_3_1_1 = "US Core 3.1.1"
USCORE_4_0_0 = "US Core 4.0.0"
USCORE_5_0_1 = "US Core 5.0.1"
SMART_1 = "SMART 1.0.0"
SMART_2 = "SMART 2.0.0"
BULK_1 = "Bulk Data Access 1.0.0"
BULK_2 = "Bulk Data Access 2.0.0"

#lists of standards grouped
US_CORE_LIST = [USCORE_3_1_1, USCORE_4_0_0, USCORE_5_0_1]
SMART_LIST = [SMART_1, SMART_2]
BULK_LIST = [BULK_1, BULK_2]


#list of standards lists
STANDARDS_LIST = [US_CORE_LIST, SMART_LIST, BULK_LIST]

#all combinations of standards in standards list
standards_combinations = itertools.product(*STANDARDS_LIST)

#function to retrieve the XML element text associated with a test procedure test ID
#parameters are the test procedure ID, XML element tree of all test IDs, and string array of applicable standards
def GetIDText(ID_to_find, all_test_IDs_element, applicable_standards):
    strToReturn = ""
    for a in all_test_IDs.iter():
        if a.tag == str(ID_to_find):
            for b in a.iter():
                if("standards" in b.attrib.keys()):
                    standards = b.attrib["standards"].strip().split(", ")
                    for s in standards:
                        if s not in applicable_standards:
                            continue
                        else:
                           strToReturn += b.text
                else:
                    strToReturn += b.text
                            
            return strToReturn
    raise Exception("ID: " + str(ID_to_find))

#retrieve test procedure from file into XML element tree
tree = ET.parse('test-procedure.xml')
root = tree.getroot()

#XML element tree of all of the test procedure's test IDs with their text
all_test_IDs = root.find("g_10_Test_Procedure_Test_IDs")

#create a Markdown file for each combination of standards
for c in standards_combinations:
    #print(c)
    with open("../docs/g10-test-procedures/" + "_".join(c).replace(" ","") + ".md", mode="w", encoding="utf8") as f:
        #write the combination of applicable standards at the top of the file
        f.write("#(g)(10) Test Procedure using: " + ", ".join(c) + "\n"*2)
        #write the contents of the file
        for i in root.find("g_10_Test_Procedure").iter():
            #determine if this element should be written based on this loop's applicable standards
            elementApplicable = True
            if("standards" in i.attrib.keys()):
                elementApplicable = False
                standards = i.attrib["standards"].strip().split(", ")
                #print(standards)
                for s in standards:
                    if s in c:
                        elementApplicable = True
                        break
            #continue if not applicable, otherwise write the name and contents of the element
            if elementApplicable == False:
                continue
            if("name" in i.attrib.keys()): 
                f.write(i.attrib["name"] + "\n")
            if(i.text.strip() != ""):
                ID_list = i.text.strip().split(", ")
                #print(i.tag)
                #print("i.text: " + i.text)
                #print(ID_list)
                for ID, counter in zip(ID_list, range(1, len(ID_list)+1)):
                    #print(ID)
                    f.write(str(counter) + "\. " + str(ID)+ ": " + GetIDText(ID, all_test_IDs, c) + "\n"*2)
                
        f.write("\n--8<-- \"includes/abbreviations.md\"")