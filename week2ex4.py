from netmiko import ConnectHandler
from getpass import getpass

router={
"host":"cisco3.lasthop.io",
"username":"pyclass",
"password":getpass(),
"device_type":"cisco_ios"
#"fast_cli":True
}

cfg=[
"ip name-server 1.1.1.1",
"ip name-server 1.0.0.1",
"ip domain-lookup"
]

net_connect=ConnectHandler(**router)
config=net_connect.send_config_set(cfg)

ping=net_connect.send_command("\n ping google.com", strip_command=False)
print(ping)
net_connect.disconnect()
