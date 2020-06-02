#!usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

router={
"host":"cisco4.lasthop.io",
"username":"pyclass",
"password":getpass(),
"device_type":"cisco_ios"
}
net_connect=ConnectHandler(**router)
device=net_connect.find_prompt().rstrip('#')
print("\n Logged into "+device+"\n")
output=net_connect.send_command('ping',expect_string=r'ip',strip_command=False,strip_prompt=False)
output+=net_connect.send_command('\n',expect_string=r'address',strip_command=False)
output+=net_connect.send_command('8.8.8.8',expect_string=r'count',strip_command=False)
output+=net_connect.send_command("\n",expect_string=r'size',strip_command=False)
output+=net_connect.send_command("\n",expect_string=r'seconds',strip_command=False)
output+=net_connect.send_command("\n",expect_string=r'commands',strip_command=False)
output+=net_connect.send_command("\n",expect_string=r'sizes',strip_command=False)
output+=net_connect.send_command("\n",expect_string=r'#',strip_command=False)

print(output)

net_connect.disconnect()

