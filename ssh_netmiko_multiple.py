import netmiko
from netmiko import ConnectHandler
import datetime
nxosv1= {
'device_type': 'cisco_nxos',
'ip': '172.16.1.90',
'username':'cisco',
'password':'cisco',
}

nxosv2= {
'device_type': 'cisco_nxos',
'ip': '172.16.1.91',
'username':'cisco',
'password':'cisco',
}

nxosv3= {
'device_type': 'cisco_nxos',
'ip': '172.16.1.92',
'username':'cisco',
'password':'cisco',
}

nxosv4= {
'device_type': 'cisco_nxos',
'ip': '172.16.1.93',
'username':'cisco',
'password':'cisco',
}

all_devices=[nxosv1,nxosv2,nxosv3,nxosv4]

start_time = datetime.datetime
for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interface brief")
    print("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(device['ip']))
    print(output)
    print(">>>>>>>>> End <<<<<<<<<")