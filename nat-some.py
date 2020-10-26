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

 
startip=u"10.10.11.1"
endip=u"10.10.11.3"
# below is to convert to integer format
ip_start = int( ipaddress.ip_address(startip) )
ip_end = int( ipaddress.ip_address(endip) )

ipdest="10.20.20.2"

# by filling below parameter, we can issue diag sys session clear when num of session reach the max
fgtip="10.10.10.1"
fgtuser="admin"
fgtpass="fortinet"

# make sure that fgt session is clear first before doing test
# ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")

# to prove stickiness using same port ?
dplist = [10044,10108,10172,10236,10300]
ipsrc = startip

for dp in dplist: 
   qstr = ipsrc+"."+str(dp)+".test"
   pkt = Ether()/IP(src=ipsrc,dst=ipdest)/UDP(sport=dp,dport=53)/DNS(rd=1,qd=DNSQR(qname = qstr))
   print ipsrc, dp, qstr
   sendp(pkt,verbose=False)
