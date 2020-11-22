from paramiko import SSHClient, AutoAddPolicy


def ssh_fgt(ipadd,portno,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd,port=portno)
    print ("Executing :"+command)
    stdin, stdout, stderr = client.exec_command(command)

    print(stdout.read())
    client.close()

fgtuser="admin"
fgtpass="fortinet"
fgtip="34.101.221.107"


ssh_fgt(fgtip, 10101, fgtuser, fgtpass, "diag sys session clear")

ssh_fgt(fgtip, 10102, fgtuser, fgtpass, "diag sys session clear")

ssh_fgt(fgtip, 10103, fgtuser, fgtpass, "diag sys session clear")

ssh_fgt(fgtip, 10104, fgtuser, fgtpass, "diag sys session clear")
