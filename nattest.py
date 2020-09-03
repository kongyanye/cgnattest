from scapy.all import *
import pdb
import random
import string
 
def get_random_string(length):
 letters = string.ascii_lowercase
 result_str = ''.join(random.choice(letters) for i in range(length))
 return(result_str)
 
startip=71
endip=90
startport=49000
endport=49100
ipdest="10.20.20.2"

 
for x in range(startip,endip):
 ipsrc = '10.10.10.'+str(x)
 for y in range(startport,endport):
		
#	pkt=Ether()/IP(src=ipsrc,dst='192.168.1.134')/UDP(sport=y,dport=53)/DNS(rd=1,qd=DNSQR(qname="www."+get_random_string(30)+"."+get_random_string(3)))
# modify dns to ip1.ip2.ip3.ip4.sport.test
	qstr = ipsrc+"."+str(y)+".test"
	pkt = Ether()/IP(src=ipsrc,dst=ipdest)/UDP(sport=y,dport=53)/DNS(rd=1,qd=DNSQR(qname = qstr))
 	print(ipsrc+" : "+str(y))
	sendp(pkt, verbose=False)
