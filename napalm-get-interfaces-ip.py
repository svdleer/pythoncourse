import json
import yaml
import pprint
yaml.version = "1.1"
from napalm import get_network_driver

user = 'sntuser'
password = 'Ilovenetworks99'


driver = get_network_driver('ios')

iosvl2 = driver('10.99.99.15', user, password)
iosvl2.open()

#yamltemplate =  [ {'get_interfaces_ip'.  } ]
ios_output = iosvl2.get_interfaces_ip()





compliance_dict={'get_interfaces_ip': {}}

for key, val in dict.items(ios_output):
        compliance_dict['get_interfaces_ip'][key] = val

print(yaml.dump(ios_output, default_flow_style=True,explicit_start=True))

#test123 = {**yamltemplate, **ios_output}
#yamltemplate.update['get_interfaces_ip'] = ios_output


#print (yaml.dump(yamltemplate))

#compliance_dict.update['get_interfaceip'] = ios_output

#print(yaml.dump(compliance,explicit_start = "True"))

#print (yaml_data)

#broken will be fixed after monday