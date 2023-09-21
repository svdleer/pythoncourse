# Import the jsontodict library
import json

# Open the sample json file and read it into variable
with open("json_example.json") as f:
    json_example = f.read()

# Print the raw json data
print(json_example)

# Parse the json into a Python dictionary
json_dict = json.loads(json_example)

# Save the interface name into a variable
int_name = json_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
json_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.2"

# Revert to the json string version of the dictionary
print(json.dumps(json_dict))