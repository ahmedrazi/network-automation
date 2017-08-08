import netmiko
from netmiko import ConnectHandler

cisco_111= {
'device_type': 'cisco_nxos',
'ip': '172.16.1.90',
'username':'cisco',
'password':'cisco',
}

net_connect = ConnectHandler(**cisco_111)
output = net_connect.find_prompt()
output2 = net_connect.send_command("sh ip int brief")
output3 = net_connect.send_command("show run | inc logging")
print(output)
print(output2)
print(output3)

## configuration changes
config_commands = ['logging buffered 19999'] # create a list of configuration commands
output4 = net_connect.send_config_set(config_commands)
print(output4)

output5 = net_connect.send_command("show run | inc logging") # verify the changes
print(output5)