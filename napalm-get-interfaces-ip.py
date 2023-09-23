# Gets the interfaces ip from router, and puts them in usable napalm compliant YAML output.

import json
import sys
import yaml
from napalm import get_network_driver


user = 'admin'
password = 'C1sco12345'
host = 'sandbox-iosxe-latest-1.cisco.com'

driver = get_network_driver('ios') 

iosvl2 = driver(host, user, password)
iosvl2.open()

json_interfaces = iosvl2.get_interfaces_ip()

preyaml_compliance = [{ 'get_interfaces_ip': json_interfaces }]

yaml_compliance = yaml.dump(preyaml_compliance, explicit_start=True, indent=3)

# Create YAML compliance file

try: 
        yamloutput = open("./yaml-compliance-outoput.txt", "w")
        yamloutput.write(yaml_compliance)
        yamloutput.close

except:
        print("Error while writing yaml compliance file\n")



iosvl2.close()