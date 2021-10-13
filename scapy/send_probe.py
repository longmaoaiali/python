# -*- coding: utf-8 -*-
import time
from scapy.all import conf, Gen, SetGen, RandMAC
from scapy.layers.dot11 import RadioTap, Dot11


def send_package(x, interval: float = 0, count: int = 0, *args, **kwargs):
    s = conf.L2socket(*args, **kwargs)

    if type(x) is str:
        x = conf.raw_layer(load=x)
    if not isinstance(x, Gen):
        x = SetGen(x)

    target_mac_set = set()
    last_time = time.time()
    try:
        for i in range(count):
            for p in x:
                now_time = time.time()
                while now_time - last_time < interval:
                    now_time = time.time()
                last_time = now_time
                # p.payload.addr2 = '88:88:88:88:88:88'
                s.send(p)
                print(p.payload.addr2)
                target_mac_set.add(p.payload.addr2)
    except KeyboardInterrupt:
        pass
    s.close()

    print()
    print(target_mac_set)
    print("Sent {} packets.".format(len(target_mac_set)))


if __name__ == "__main__":
    iface = 'WLAN 3'
    the_interval = 0.1
    the_count = 10000
    mac_head = 'e4:46:da'

    print("iface={}, packs={}, machead={}, interval={}".format(iface, the_count, mac_head, the_interval))
    start_time = time.time()
    print("start time: {}".format(start_time))
    print("Press CTRL+C to Abort\n")

    send_package(RadioTap() /
                 Dot11(type=0, subtype=4,
                       addr1="ff:ff:ff:ff:ff:ff",
                       addr2=RandMAC(mac_head),
                       addr3="ff:ff:ff:ff:ff:ff"),
                 iface=iface, count=the_count, interval=the_interval)

    end_time = time.time()
    print("end time={}, spend time={}".format(end_time, end_time - start_time))
