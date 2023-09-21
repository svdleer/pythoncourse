import jinja2
import yaml
import os
import netmiko
from netmiko import ConnectHandler
import time

# Device config

deviceauth = { 'device_type':  'cisco_ios', 
    'username': 'sntuser',
    'password': 'Ilovenetworks99',
    'secret': 'cisco',  
    'fast_cli': 'false'
    }

# Jinja enviroment 

j2_env = jinja2.Environment(loader = jinja2.FileSystemLoader('./jinja-templates'))
template = j2_env.get_template('jinja-template.j2')

# Open YAML config

yaml_cfg_file = open('./jinja-data/loopbacks.yml')
config_data = yaml.load(yaml_cfg_file, Loader=yaml.FullLoader)

# Loop through config data yaml

for host in config_data:
    # Create config file path for file creating
    config_file = f'./j2-config-files/{host}-config-file.cfg'
    # Open new config file and write data
    with open(config_file, "w") as new_config_file:
        new_config_file.write(template.render(config_data[host]))
        print (config_data[host]['mgmt_ip'])

    deviceauth.update (host=config_data[host]['mgmt_ip'])
    device_connection = netmiko.ConnectHandler(**deviceauth)
    device_connection.enable()
    device_connection.send_config_set
    result = device_connection.send_config_from_file(f'./j2-config-files/{host}-config-file.cfg')
    print(result)
    #device_connection.find_prompt()
    time.sleep(1)
    result = device_connection.save_config() 
    print(result)
    device_connection.disconnect()

