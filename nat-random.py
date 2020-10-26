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

 
def get_random_string(length):
 letters = string.ascii_lowercase
 result_str = ''.join(random.choice(letters) for i in range(length))
 return(result_str)

startip=u"10.10.11.1"
endip=u"10.10.11.3"
# below is to convert to integer format
ip_start = int( ipaddress.ip_address(startip) )
ip_end = int( ipaddress.ip_address(endip) )

startport=10001
endport=10300
#startport=10001
#endport=10002

ipdest="10.20.20.2"

# by filling below parameter, we can issue diag sys session clear when num of session reach the max
fgtip="10.10.10.1"
fgtuser="admin"
fgtpass="fortinet"

numport=0
maxportperuser=64

sleepcounter = 1
# make sure that fgt session is clear first before doing test
ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")
 
for x in range(ip_start,ip_end+1):
 # need to convert back from integer to string IP-format 
 ipsrc = str(ipaddress.ip_address(x))
 for y in range(startport,endport+1):
                
# modify dns to ip1.ip2.ip3.ip4.sport.test
        dp = endport-(y-startport)
        qstr = ipsrc+"."+str(dp)+".test"

#        pkt = Ether()/IP(src=ipsrc,dst=ipdest)/UDP(sport=y,dport=53)/DNS(rd=1,qd=DNSQR(qname = qstr))
        pkt = Ether()/IP(src=ipsrc,dst=ipdest)/UDP(sport=dp,dport=53)/DNS(rd=1,qd=DNSQR(qname = qstr))
        print(ipsrc+" : "+str(dp))
        
        numport = numport + 1
        if ( numport > maxportperuser ):
            ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")
            numport = 0
 
        sendp(pkt, verbose=False)
# to make sure no packet loss received on the server side because serverside will do a print out to screen
# every 100 seconds
        if ( sleepcounter == 100 ):
           time.sleep(1)
           sleepcounter = 0
        else:
           sleepcounter = sleepcounter+1
