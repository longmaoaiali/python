import time
from scapy.all import conf, Gen, SetGen, RandMAC
from scapy.layers.dot11 import RadioTap, Dot11
from scapy.all import *



netSSID = 'testSSID' #Network name here
#iface = 'WLAN'   #Interface name here

iface = conf.iface

dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', 
addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33')
beacon = Dot11Beacon(cap='ESS+privacy')
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))

rsn = Dot11Elt(ID='RSNinfo', info=(
'\x01\x00'#RSN Version 1
'\x00\x0f\xac\x02'#Group Cipher Suite : 00-0f-ac TKIP 
'\x02\x00'#2 Pairwise Cipher Suites (next two lines)
'\x00\x0f\xac\x04'#AES Cipher
'\x00\x0f\xac\x02'#TKIP Cipher
'\x01\x00'#1 Authentication Key Managment Suite (line below)
'\x00\x0f\xac\x02'#Pre-Shared Key
'\x00\x00'))#RSN Capabilities (no extra capabilities)
frame = RadioTap()/dot11/beacon/essid/rsn
frame.show()
print("\nHexDump of frame:")
hexdump(frame)
#raw_input("\nPress enter to start\n")
sendp(frame, iface=iface, inter=0.100, loop=1)