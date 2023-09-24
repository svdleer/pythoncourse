from nornir import InitNornir
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

nr = InitNornir("config.yml")

d = "Test interface Dont touch"
#The f below is an f string - d is placed in the string
dconfig = [ "interface gi1", f"description {d}", ]

rtrs = nr.filter((F(platform__contains="ios") & F(groups__contains="devnet")))

result = rtrs.run(netmiko_send_config, config_commands=dconfig)
print_result(result)