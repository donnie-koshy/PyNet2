from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

nexus={

"host":"nxos2.lasthop.io",
"username":"pyclass",
"password":getpass(),
"device_type":"cisco_nxos",
"global_delay_factor":2
}

