from nornir import InitNornir
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli

nr = InitNornir("config.yml")

rtrs = nr.filter((F(groups__contains="devnet")))

result = rtrs.run(task=napalm_get, getters=["interfaces"])
print_result(result)