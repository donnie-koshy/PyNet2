from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pprint import pprint


router={
"host":"cisco4.lasthop.io",
"username":"pyclass",
"password":getpass(),
"device_type":"cisco_ios"
}

net_session=ConnectHandler(**router)
version=net_session.send_command("show version", use_textfsm=True)
print ("Router version")
print ("--------------")
pprint(version)
print ("\n LLDP Neighbour table"+"\n"+"----------------------")
lldp_neigh=net_session.send_command("show lldp neighbors", use_textfsm=True)
pprint (lldp_neigh)

print("Remote Device interface is "+lldp_neigh[0]['neighbor_interface'])
net_session.disconnect()
