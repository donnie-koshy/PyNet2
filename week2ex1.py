#!usr/bin/env python
from netmiko import ConnectHandler,file_transfer
from getpass import getpass

router={
"host":"cisco4.lasthop.io",
"username":"pyclass",
"password":getpass(),
"device_type":"cisco_ios"
}
net_connect=ConnectHandler(**router)
device=net_connect.find_prompt().rstrip('#')
print("\n Logged into "+device)
#output=net_connect.send_command_timing("ping")
output=net_connect.send_command("ping",expect_string=':')
print(output)
print(net_connect.find_prompt())
net_connect.disconnect()

