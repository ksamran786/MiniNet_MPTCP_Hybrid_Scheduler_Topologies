
#!/usr/bin/python\
\
""" Script to use MPTCP in Mininet. Run on commandline as, python 2host-2switch-mptcp.py """\
\
from mininet.net import Mininet\
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch\
from mininet.cli import CLI\
from mininet.log import setLogLevel\
from mininet.link import Link, TCLink\
\
def topology():\
    "Create a network."\
  # Defining network \
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )\
    print "*** Creating nodes"\
  # Adding hosts, switches and controller\
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )\
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )\
    s1 = net.addSwitch( 's1' )\
    s2 = net.addSwitch( 's2' )\
    c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6653 )\
    \
    print "*** Creating links"\
\
  # net.addLink(s1, h2, 2, 0)\
  # net.addLink(h1, s1, 0, 1)\
  # net.addLink(s2, h2, 2, 0)\
  # net.addLink(h1, s2, 0, 1)\
  \
  # Adding links and link bandwidth\
    net.addLink(h1, s1, intfName1='h1-eth0',bw=100)\
    net.addLink(h2, s1, intfName1='h2-eth0', bw=100)\
    net.addLink(h1, s2, intfName1='h1-eth1', bw=100)\
    net.addLink(h2, s2, intfName1='h2-eth1', bw=100)\
    \
  # Commands for identifyig the second interfaces of h1 and h2 hosts\
    h1.cmd('ifconfig h1-eth1 10.0.10.1 netmask 255.255.255.0')\
    h2.cmd('ifconfig h2-eth1 10.0.10.2 netmask 255.255.255.0')\
\
    print "*** Starting network"\
    net.build()\
    c0.start()\
    s1.start( [c0] )\
    s2.start( [c0] )\
\
    print "*** Running CLI"\
    CLI( net )\
\
    print "*** Stopping network"\
\
    net.stop()\
\
if __name__ == '__main__':\
\
    setLogLevel( 'info' )\
\
    topology()}
