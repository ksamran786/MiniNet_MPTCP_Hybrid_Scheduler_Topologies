
#!/usr/bin/python\
"""\
3 hosts (h1 h2 h3) connected via switch on one subnet. Hosts h1 h2 also connected directly via another interace path.\
iperf -s h2, and h1 and h3 as client.\
h1-eth1 10.0.10.11,h2-eth1 10.0.10.22, h3-eth0 10.0.10.33\
Pre-req Enabeled: 1. Mptcp enabled, 2. sudo sysctl net.ipv4.tcp_congestion_control=reno\
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
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.10.33/24' )\
    s1 = net.addSwitch ( 's1')\
\
    print "*** Creating links"\
    \
    #direct connection between h1 and h2\
    net.addLink(h1, h2, intfName1='h1-eth0', intfName2='h2-eth0',bw=100)\
    # connection via switch s1\
    net.addLink(h1, s1, intfName1='h1-eth1', intfName2='s1-eth1', bw=100)\
    net.addLink(h2, s1, intfName1='h2-eth1', intfName2='s1-eth2', bw=100)\
    net.addLink(h3, s1, intfName1='h3-eth0', intfName2='s1-eth0', bw=100)\
    h1.cmd('ifconfig h1-eth1 10.0.10.11 netmask 255.255.255.0')\
    h2.cmd('ifconfig h2-eth1 10.0.10.22 netmask 255.255.255.0')\
\
    print "*** Starting network"\
    net.build()\
   # start s1 switch\
    s1.start('')\
    s1.cmd('switch s1 start')\
   # add flows in switch\
    s1.cmd('ovs-ofctl add-flow s1 in_port=1,actions:output=2')\
    s1.cmd('ovs-ofctl add-flow s1 in_port=3,actions:output=2')\
    s1.cmd('ovs-ofctl add-flow s1 in_port=2,actions:output=1,3')\
\
    print "*** Running CLI"\
    CLI( net )\
    print "*** Stopping network"\
    net.stop()\
\
if __name__ == '__main__':\
\
    setLogLevel( 'info' )\
\
    topology()\
\
}
