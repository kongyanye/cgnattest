from scapy.all import *
from paramiko import SSHClient, AutoAddPolicy
import pdb
import random
import string
import ipaddress

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

# in python2.7 must use unicode so must use u'xxx'

startip=u'10.10.10.1'
endip=u'10.10.20.254'
# below is to convert to integer format
ip_start = int( ipaddress.ip_address(startip.decode('utf-8')) )
ip_end = int( ipaddress.ip_address(decode('utf-8')) )

startport=9949
endport=10700
ipdest="10.20.20.2"

# by filling below parameter, we can issue diag sys session clear when num of session reach the max
fgtip="10.10.10.1"
fgtuser="admin"
fgtpass="fortinet"

numport=0
maxportperuser=302

# make sure that fgt session is clear first before doing test
ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")
 
for x in range(ip_start,ip_end+1):
 # need to convert back from integer to string IP-format 
 ipsrc = str(ipaddress.ip_address(x))
 for y in range(startport,endport+1):
                
# modify dns to ip1.ip2.ip3.ip4.sport.test
        qstr = ipsrc+"."+str(y)+".test"
        pkt = Ether()/IP(src=ipsrc,dst=ipdest)/UDP(sport=y,dport=53)/DNS(rd=1,qd=DNSQR(qname = qstr))
        print(ipsrc+" : "+str(y))
        
        numport = numport + 1
        if ( numport > maxportperuser ):
            ssh_fgt(fgtip, fgtuser, fgtpass, "diag sys session clear")
            numport = 0

        sendp(pkt, verbose=False)



'''
this module works !!
>>> a='10.10.10.1'
>>> b='10.10.13.2'
>>> x=int(ipaddress.ip_address(a))
>>> y=int(ipaddress.ip_address(b))
>>> print (x,' ',y)
168430081   168430850
>>> for i in range(x,y):
...     print ipaddress.ip_address(i)
  File "<stdin>", line 2
    print ipaddress.ip_address(i)
          ^
SyntaxError: invalid syntax
>>> for i in range(x,y+1):
...     print (ipaddress.ip_address(i))
...
10.10.10.1
10.10.10.2
10.10.10.3
10.10.10.4
10.10.10.5
'
