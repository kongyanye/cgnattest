
from scapy.all import *
import string
import pdb

ipadd="10.20.20.2"

print("I am listening at "+ipadd+" port 53, and will stop when break\n\n")
buffer = 100
sourceipbefore = ""

while True:
    dengar=sniff(count=buffer,filter="host "+ipadd+" and udp and port 53")
    for x in range(0,buffer-1):
       qn = dengar[x]['IP']['UDP']['DNS']['DNSQR'].qname
       titik = [ pos for pos,char in enumerate(qn) if char == "."]
#       pdb.set_trace()
       if ( len(titik)>3 ):
          sourceiponly = qn[0:titik[3]]

          if ( sourceiponly != sourceipbefore ):
             if ( sourceipbefore != "" ):
                 print ("**** SOURCE IP CHANGED ****")
             sourceipbefore = sourceiponly

          print(  qn + "-----> "+ dengar[x]['IP'].src+" "+ str(dengar[x]['UDP'].sport) )



''''
>>> a[3]['IP']['UDP']
<UDP  sport=23233 dport=domain len=64 chksum=0x3162 |<DNS  id=0 qr=0 opcode=QUERY aa=0 tc=0 rd=1 ra=0 z=0 ad=0 cd=0 rcode=ok qdcount=1 ancount=0 nscount=0 arcount=0 qd=<DNSQR  qname='www.wlqrwnwpgtlnnsrrkdshmlufqsqbkh.wxy.' qtype=A qclass=IN |> an=None ns=None ar=None |>>
>>> a[3]['IP']['UDP']['DNS']['DNSQR'].qname
'www.wlqrwnwpgtlnnsrrkdshmlufqsqbkh.wxy.'
>>> a[3]['IP']
<IP  version=4 ihl=5 tos=0x0 len=84 id=1 flags= frag=0 ttl=64 proto=udp chksum=0xf68c src=192.168.1.53 dst=192.168.1.134 |<UDP  sport=23233 dport=domain len=64 chksum=0x3162 |<DNS  id=0 qr=0 opcode=QUERY aa=0 tc=0 rd=1 ra=0 z=0 ad=0 cd=0 rcode=ok qdcount=1 ancount=0 nscount=0 arcount=0 qd=<DNSQR  qname='www.wlqrwnwpgtlnnsrrkdshmlufqsqbkh.wxy.' qtype=A qclass=IN |> an=None ns=None ar=None |>>>
>>> a[3]['IP'].src
'192.168.1.53'
>>> a[3]['UDP'].sport
23233

issue : if used like loop with 1 packet, there is possible skip !

'''
