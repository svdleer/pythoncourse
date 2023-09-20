import netmiko
from netmiko import ConnectHandler
import textfsm
from ntc_templates.parse import parse_output


SW1 = { 'device_type':  'cisco_ios', 
        'host': '10.99.99.14',
        'username': 'sntuser',
        'password': 'Ilovenetworks99',
        #'secret': 'cisco',  
        }
device_connection = netmiko.ConnectHandler(**SW1)
device_connection.enable

list_response = device_connection.send_command("show ip interface brief", use_textfsm=True)
print(list_response) 

not_connect_interfaces = [item['intf'] for item in list_response if item['status'] == 'up' ]
print(not_connect_interfaces)