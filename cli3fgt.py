from paramiko import SSHClient, AutoAddPolicy
import sys

def ssh_fgt(ipadd,portno,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd,port=portno)
    print ("Executing :"+command)
    stdin, stdout, stderr = client.exec_command(command)
# use decode to translate b' and \n
    print(stdout.read().decode())
    client.close()

fgtuser="admin"
fgtpass="fortinet"
fgtip="34.101.221.107"

perintah=sys.argv[1:]

if not perintah:
    print("Must have a command to execute in 3 fgt !")
    exit()

# 10101 - fgt1 , 10102 - fgt2, 10103 - fgt3, 10104 -fgt-lb
strperintah = ' '.join(perintah)
print(strperintah)
for x in range(10101,10104+1) :
    ssh_fgt(fgtip, x, fgtuser, fgtpass, strperintah )
