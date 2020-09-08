import ipaddress
import sys
import math
import pdb

try:
    searchip = sys.argv[1]
    searchport = sys.argv[2]
except:
    print("Must have 2 argument ext ip and port: x.x.x.x yyyy")
    print("optional 3rd parameter is blocksize")
    exit()

try:
    blocksize = int(sys.argv[3])
except:
    blocksize = 1000

extstartip='10.1.1.1'
extendip='10.1.1.3'
intstartip='192.168.1.1'
intendip='192.168.1.100'
portstart = 5117
portend = 65533

print(f'External IP :{extstartip} - {extendip}, Internal IP :{intstartip} - {intendip}')
print(f'Default external port is {portstart} - {portend}')
print(f'Max Port Block Size per Internal IP :{blocksize}')
print(f'{searchip} : {searchport} belongs to ??')

extno = int(ipaddress.ip_address(searchip)) - int(ipaddress.ip_address(extstartip)) + 1
sport = 60417* (extno-1) + ( int(searchport) - 5117 ) + 1
ipinternalno = math.floor( sport / blocksize)

resultinternalip = ipaddress.ip_address( int (ipaddress.ip_address(intstartip)) + ipinternalno )

#print(f'Searched IP:port is  no# {extno} - {sport} - internal ip no {ipinternalno}')
print ("----->", resultinternalip)





