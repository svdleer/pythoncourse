

# Import libraries
import requests, urllib3, sys, yaml

# Add parent directory to path to allow importing common vars
sys.path.append("..") # noqa
from env_lab import IOS_XE_1 as device # noqa

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setup base variable for request
restconf_headers = {"Accept": "application/yang-data+json",
                    "Content-Type": "application/yang-data+json"}
restconf_base = "https://{ip}:{port}/restconf/data"
interface_url = restconf_base + "/ietf-interfaces:interfaces/interface={int_name}"

# New Loopback Details
loopback = {"name": "Loopback101",
            "description": "Demo interface by RESTCONF",
            "ip": "192.168.101.1",
            "netmask": "255.255.255.0"}

# Setup data body to create new loopback interface
data = {
    "ietf-interfaces:interface": {
        "name": loopback["name"],
        "description": loopback["description"],
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": loopback["ip"],
                    "netmask": loopback["netmask"]
                }
            ]
        }
    }
}

# Create URL and send RESTCONF request to device
url = interface_url.format(ip = device["host"],
                           port = device["restconf_port"],
                           int_name = loopback["name"]
                          )
print("URL: {}\n".format(url))

r = requests.put(url,
        headers = restconf_headers,
        auth=(device["username"], device["password"]),
        json = data,
        verify=False)

# Print returned data
print("PUT Request Status Code: {}".format(r.status_code))