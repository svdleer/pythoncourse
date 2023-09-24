import json
from pyntc import ntc_device as NTC


user = 'developer'
password = 'lastorangerestoreball8876'
hostname = 'sandbox-iosxe-recomm-1.cisco.com'

l2=NTC(host=hostname, username=user,password=password, secret="cisco", device_type="cisco_ios_ssh")
l2.open()
f=l2.facts

print (f)
print(json.dumps(f,indent=4))
l2.close()