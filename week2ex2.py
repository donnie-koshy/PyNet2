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

net_connect=ConnectHandler(**nexus)

device=net_connect.find_prompt().rstrip('#')
print ("Logged into "+device)

time_before=datetime.now().strftime("%H:%M:%S")
print("Time before execution  "+time_before)

output=net_connect.send_command("\n show lldp neighbors detail")

time_after=datetime.now().strftime("%H:%M:%S")

print(output)
print("Time after execution "+time_after+"\n")

output_delay=net_connect.send_command("\n show lldp neighbors detail",delay_factor=8)
print (output_delay)
time_after=datetime.now().strftime("%H:%M:%S")
print("Time after execution "+time_after+"\n")


