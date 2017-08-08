import paramiko
import time

HOST='192.168.1.159'
USER='rahmed'
PASS='asdf'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST,username=USER,password=PASS)

ssh_connection = ssh_client.invoke_shell()

ssh_connection.send("uname\n")
ssh_connection.send("date\n")

output = ssh_connection.recv(1111).decode(encoding="utf-8")
time.sleep(1)
print(output)
ssh_client.close()