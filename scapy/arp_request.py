#!/usr/bin/python3
# -*- coding=utf-8 -*-
import sys
from scapy.all import *


#配置各种信息，以便调用
localmac = 'D0:C6:37:28:D9:DF'
#localmac = '84:FD:D1:E6:C0:BC'
localip = '192.168.1.6'
destip = '192.168.1.1'
ifname = 'WLAN'




#源MAC为本地MAC# 
#目的MAC为广播#
#操作码为1（请求）#
#由于多个网卡所以需要指派iface 二层包需要指派接口，三层包会查路由不需要指派接口#
#verbose=False 关闭终端的打印提示#
arp_replypackage = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF')/ARP(op=1, hwsrc=localmac, hwdst='00:00:00:00:00:00', psrc=localip, pdst=destip), iface = ifname, timeout=1, verbose=False)
print(arp_replypackage)
print(arp_replypackage[0]) #元组第一个对象元素
print(type(arp_replypackage[0])) #打印出type后直接google该类
print(arp_replypackage[0].res)
#调用类的方法，生成list


print(arp_replypackage[0].res[0]) #提取清单中的第一个元组
print(arp_replypackage[0].res[0][1]) #提取清单中的第一个元组 第二个对象即收的包 这里打印是16进制
print(arp_replypackage[0].res[0][1].getlayer(ARP).fields) #上面的16进制转换为arp的字典
print(arp_replypackage[0].res[0][1].getlayer(ARP).fields['hwsrc']) #得到arp reply字典的hwsrc字段

#res: the list of packets，产生由收发数据包所组成的清单（list）
arp_replylist = arp_replypackage[0].res

print(arp_replylist[0][1])          #默认是print(arp_replylist[0][1][0]) 
print(arp_replylist[0][1].fields)

print(arp_replylist[0][1][0])
print(arp_replylist[0][1][0].fields) #数据链路层封装的以太网帧头

print(arp_replylist[0][1][1])
print(arp_replylist[0][1][1].fields) #ARP包 head + body

#print(arp_replylist[0][1][2])

#result_list[0][1][0]，[0]表示第一组数据包（收发），[1]，表示收包（0为发包），[1]表示ARP头部
#print(result_list[0][1][1].fields) ARP头部字段
#{'pdst': '202.100.1.138', 'hwtype': 1, 'hwdst': '00:0c:29:8d:5c:b6', 'plen': 4, 'ptype': 2048, 'hwsrc': '00:0c:29:43:52:cf', 'op': 2, 'hwlen': 6, 'psrc': '202.100.1.139'}
print('IP地址: ' + arp_replylist[0][1][1].fields['psrc'] + ' MAC地址: ' + arp_replylist[0][1][1].fields['hwsrc'])