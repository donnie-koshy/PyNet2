from netmiko import ConnectHandler
from getpass import getpass

uname="pyclass"

nxos1={
"host":"nxos1.lasthop.io",
"username":uname,
"password":getpass(),
"device_type":"cisco_nxos"
}

nxos2={
"host":"nxos2.lasthop.io",
"username":uname,
"password":getpass(),
"device_type":"cisco_nxos"
}

output=""
count=1

for device in (nxos1,nxos2):
    net_connect=ConnectHandler(**device)
    net_connect.send_config_from_file("vlan.txt")
    net_connect.save_config()
    output=net_connect.send_command("show vlan brief",strip_prompt=False)

    print ("Output from Nexus device#"+str(count))
    count+=1
    print(output)
    net_connect.disconnect()
