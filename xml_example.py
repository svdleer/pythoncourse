# Import the xmltodict library
import xmltodict

# Open the sample xml file and read it into variable
#with open("./11 data_manipluation/xml/xml_example.xml") as f:
with open("xml_example.xml") as f:
    xml_example = f.read()

# Print the raw XML data
print(xml_example)

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)

# Save the interface name into a variable using XML nodes as keys
int_name = xml_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.0.2"

# Revert to the XML string version of the dictionary
print(xmltodict.unparse(xml_dict))