# first parameter is tcpfirst or udpfirst
# second parameter is diff - or leave empty if it is same port tcp and udp

from scapy.all import *
from paramiko import SSHClient, AutoAddPolicy
import pdb
import random
import string
import ipaddress
import time
import sys

def ssh_fgt(ipadd,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd)
    stdin, stdout, stderr = client.exec_command(command)

    print(stdout.read())
    client.close()


srcip='10.10.10.111'
dstip='10.20.20.2'
sportstart=20001
destport=80
udpnumber=5
tcpnumber=6

try :
   urutan = sys.argv[1]
   print (sys.argv[1])
except :
   urutan = 'udpfirst'

try:
   portno = sys.argv[2]
   tcpudp = 'diff'
except :
   tcpudp ='same'

fgtip="10.10.1.1"
fgtuser="admin"
fgtpass="fortinet"

ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")

print("Blasting TCP and UDP packet")
print("---------------------------")

if ( urutan=='tcpfirst' ):
  for x in range(sportstart,sportstart+tcpnumber):

    sourceport = x

    pkt=Ether()/IP(src=srcip,dst=dstip)/TCP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("TCP  ",srcip,":",sourceport,"  --->",dstip,":",destport)

  for x in range(sportstart,sportstart+udpnumber):

    if ( tcpudp == 'diff' ):
        sourceport = x+1000
    else:
        sourceport = x

    pkt=Ether()/IP(src=srcip,dst=dstip)/UDP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("UDP  ",srcip,":",sourceport,"  --->",dstip,":",destport)

else :

  for x in range(sportstart,sportstart+udpnumber):

    if ( tcpudp == 'diff' ):
        sourceport = x+1000
    else:
        sourceport = x

    pkt=Ether()/IP(src=srcip,dst=dstip)/UDP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("UDP  ",srcip,":",sourceport,"  --->",dstip,":",destport)

  for x in range(sportstart,sportstart+tcpnumber):

    sourceport = x

    pkt=Ether()/IP(src=srcip,dst=dstip)/TCP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("TCP  ",srcip,":",sourceport,"  --->",dstip,":",destport)



