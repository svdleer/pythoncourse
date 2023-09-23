import json

from napalm import get_network_driver

user = 'sntuser'
password = 'Ilovenetworks99'


driver = get_network_driver('ios')

iosvl2 = driver('10.99.99.15', user, password)
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent=4))
iosvl2.close()
