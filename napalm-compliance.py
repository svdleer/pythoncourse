import json

from napalm import get_network_driver

user = 'sntuser'
password = 'Ilovenetworks99'

driver = get_network_driver('ios')

iosvl2 = driver('10.99.99.15', user, password, timeout=30, optional_args={"read_timeout_override": 90})
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_facts()


iosvl2.load_replace_candidate('./replace-cfg.cfg')

print(iosvl2.compare_config())
try:
    choice = raw_input("\nWould you like to commit these changes? [yN]: ")
except NameError:
    choice = input("\nWould you like to commit these changes? [yN]: ")
if choice == "y":
    print("Committing ...")
    iosvl2.commit_config()
else:
    print("Discarding ...")
    iosvl2.discard_config()


# not finished
