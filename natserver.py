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

