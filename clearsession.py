from scapy.all import *
from paramiko import SSHClient, AutoAddPolicy
import pdb
import random
import string
import ipaddress
import time


def ssh_fgt(ipadd,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd)
    stdin, stdout, stderr = client.exec_command(command)

    print(stdout.read())
    client.close()


fgtip="10.10.1.1"
fgtuser="admin"
fgtpass="fortinet"

ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")
