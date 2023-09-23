
# Import libraries
import requests, urllib3
import sys

# Add parent directory to path to allow importing common vars
sys.path.append("..") # noqa
from env_lab import IOS_XE_1 as device # noqa

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setup base variable for request
restconf_headers = {"Accept": "application/yang-data+json"}
restconf_base = "https://{ip}:{port}/restconf/data"
interface_url = restconf_base + "/ietf-interfaces:interfaces/interface={int_name}"

# Create URL and send RESTCONF request to core1 for GigE2 Config
url = interface_url.format(ip = device["host"],
                           port = device["restconf_port"],
                           int_name = "Loopback101"
                          )
print("URL: {}\n".format(url))

r = requests.delete(url,
        headers = restconf_headers,
        auth=(device["username"], device["password"]),
        verify=False)

# Print returned data
print("DELETE Request Status Code: {}".format(r.status_code))

