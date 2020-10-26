from scapy.all import *

def kirim(srcip,dstip,sourceport,destport):
    pkt=Ether()/IP(src=srcip,dst=dstip)/TCP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("TCP  ",srcip,":",sourceport,"  --->",dstip,":",destport)

    pkt=Ether()/IP(src=srcip,dst=dstip)/UDP(sport=sourceport,dport=destport)
    sendp(pkt, verbose=False)
    print("UDP  ",srcip,":",sourceport,"  --->",dstip,":",destport)


kirim('10.10.10.1','10.20.20.2',10000,80)
kirim('10.10.10.1','10.20.20.3',10000,80)
kirim('10.10.10.1','10.20.20.4',10000,80)

kirim('10.10.10.1','10.20.20.2',10000,8080)
kirim('10.10.10.1','10.20.20.3',10000,8080)
kirim('10.10.10.1','10.20.20.4',10000,8080)

kirim('10.10.10.1','10.20.20.2',20000,8080)
kirim('10.10.10.1','10.20.20.3',20000,8080)
kirim('10.10.10.1','10.20.20.4',20000,8080)




