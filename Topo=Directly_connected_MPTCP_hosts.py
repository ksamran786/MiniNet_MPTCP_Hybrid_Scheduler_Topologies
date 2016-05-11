{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
#!/usr/bin/python\
"""\
2 hosts (h1 h2 directly connected) via two interfaces to utilize the multipath.\
iperf result show twice the bandwidth i.e. for two 100Mbps links aroung 188Mbps.\
\
"""\
\
from mininet.net import Mininet\
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch\
from mininet.cli import CLI\
from mininet.log import setLogLevel\
from mininet.link import Link, TCLink\
\
def topology():\
    "Create a network."\
    net = Mininet( controller=None, link=TCLink, switch=OVSKernelSwitch )\
    print "*** Creating nodes"\
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )\
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )\
\
    print "*** Creating links"\
\
    net.addLink(h1, h2, intfName1='h1-eth0', intfName2='h2-eth0',bw=100)\
    net.addLink(h1, h2, intfName1='h1-eth1', intfName2='h2-eth1', bw=100)\
    h1.cmd('ifconfig h1-eth1 10.0.10.1 netmask 255.255.255.0')\
    h2.cmd('ifconfig h2-eth1 10.0.10.2 netmask 255.255.255.0')\
    print "*** Starting network"\
    net.build()\
    print "*** Running CLI"\
    CLI( net )\
    print "*** Stopping network"\
    net.stop()\
\
if __name__ == '__main__':\
\
    setLogLevel( 'info' )\
\
    topology()}