from paramiko import SSHClient, AutoAddPolicy
import pdb

client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('10.10.10.1',username='admin',password='fortinet')

stdin, stdout, stderr = client.exec_command('get system status')

print(stdout.read())

client.close()

