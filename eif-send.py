from scapy.all import *

def kirim(srcip,dstip,sourceport,destport):
#    pkt=Ether()/IP(src=srcip,dst=dstip)/TCP(sport=sourceport,dport=destport)
#    sendp(pkt, verbose=False)
#    print("TCP  ",srcip,":",sourceport,"  --->",dstip,":",destport)

    pkt=Ether()/IP(src=srcip,dst=dstip)/UDP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("UDP  ",srcip,":",sourceport,"  --->",dstip,":",destport)


kirim('10.10.10.101','10.20.20.200',10000,80)



