import json
import yaml

from napalm import get_network_driver

user = 'sntuser'
password = 'Ilovenetworks99'


driver = get_network_driver('ios')

iosvl2 = driver('10.99.99.15', user, password)
iosvl2.open()

ios_output = iosvl2.get_interfaces_ip()
print(yaml.dump(ios_output))



