import json

from napalm import get_network_driver

user = 'admin'
password = 'C1sco12345'
host = 'sandbox-iosxe-latest-1.cisco.com'


driver = get_network_driver('ios')

iosvl2 = driver(host, user, password, timeout=30, optional_args={"read_timeout_override": 90})
iosvl2.open()

validation = iosvl2.compliance_report('./compliance.yaml')
print(json.dumps(validation, indent=4))

iosvl2.close()

