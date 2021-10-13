# -*- coding: utf-8 -*-
import time
from scapy.all import conf, Gen, SetGen, RandMAC
from scapy.layers.dot11 import RadioTap, Dot11
from scapy.all import *


print({Dot11Beacon:%Dot11.addr3%\ ˓→t%Dot11Beacon.info%\t%PrismHeader.channel%\t%Dot11Beacon.cap%});
sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface="WLAN 3")

sendp(RadioTap()/
	Dot11(addr1="ff:ff:ff:ff:ff:ff",
	addr2="00:01:02:03:04:05",
	addr3="00:01:02:03:04:05")/
	Dot11Beacon(cap="ESS", timestamp=1)/
	Dot11Elt(ID="SSID", info="liuyutest")/
	Dot11EltRates(rates=[130, 132, 11, 22])/
	Dot11Elt(ID="DSset", info="\x03")/
	Dot11Elt(ID="TIM", info="\x00\x01\x00\x00"),
	iface="WLAN 3", loop=1)
	
sniff(iface="ath0", prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\ ˓→t%Dot11Beacon.info%\t%PrismHeader.channel%\t%Dot11Beacon.cap%}"))

   


