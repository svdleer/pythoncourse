from ncclient import manager
import xmltodict

host = 'sandbox-iosxe-latest-1.cisco.com'
user = 'admin'
password = 'C1sco12345'

with manager.connect(host=host, port=830, username=user, password=password, device_params={'name':'iosxe'}) as m:
    c = m.get_config(source='running').data_xml
    with open("sandbox.xml", "w") as f:
        f.write(c)

#print (c) 
print(xmltodict.parse(c))

