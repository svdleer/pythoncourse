import json

from napalm import get_network_driver

user = 'sntuser'
password = 'Ilovenetworks99'

driver = get_network_driver('ios')

iosvl2 = driver('10.99.99.15', user, password, timeout=30, optional_args={"read_timeout_override": 90})
iosvl2.open()

validation = iosvl2.compliance_report('./compliance.yaml')
print(json.dumps(validation, indent=4))

iosvl2.close()

