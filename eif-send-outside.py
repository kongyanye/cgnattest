from scapy.all import *
import sys

def kirim(srcip,dstip,sourceport,destport):
#    pkt=Ether()/IP(src=srcip,dst=dstip)/TCP(sport=sourceport,dport=destport)
#    sendp(pkt, verbose=False)
#    print("TCP  ",srcip,":",sourceport,"  --->",dstip,":",destport)

    pkt=Ether()/IP(src=srcip,dst=dstip)/UDP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("UDP  ",srcip,":",sourceport,"  --->",dstip,":",destport)


dstip='10.20.20.202'
#dstport needs to be changed after getting the destport from fgt sniffer
try :
   dstport=int(sys.argv[1])
except :
   print("Please enter one argument, which is the destination port")
   exit()

kirim('10.20.20.200', dstip,80,dstport)
kirim('10.20.20.3', dstip,10080,dstport)
kirim('10.20.20.4', dstip,20080,dstport)
kirim('10.20.20.5', dstip,30080,dstport)
kirim('10.20.20.5', dstip,40080,dstport)



