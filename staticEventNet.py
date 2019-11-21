from mininet.net import Mininet
from mininet.node import Node, Switch, RemoteController
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI

import mininet.ns3
from mininet.ns3 import WIFISegment

import ns.core
import ns.network
import ns.wifi
import ns.csma
import ns.wimax
import ns.uan
import ns.netanim

from mininet.opennet import *

def staticEventNet():

    net = Mininet()

    net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6653)

    sw0 = net.addSwitch('sw0', ip=None, failMode='standalone')
    ap0 = net.addSwitch('ap0', ip=None, failMode='standalone')
    ap1 = net.addSwitch('ap1', ip=None, failMode='standalone')
    ap2 = net.addSwitch('ap2', ip=None, failMode='standalone')

    info( '*** Creating Network\n' )
    h0 = net.addHost( 'h0' )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )

    wifi = WIFISegment ()
    wifi.addAp(ap0, channelNumber=11, ssid="opennet_0")
    wifi.addAp(ap1, channelNumber=11, ssid="opennet_1")
    wifi.addAp(ap2, channelNumber=11, ssid="opennet_2")

    wifi.addAdhoc( h0 )
    wifi.addAdhoc( h1 )
    wifi.addAdhoc( h2 )

    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )
    h2.setIP( '192.168.123.3/24' )

    mininet.ns3.setPosition(ap0, 100, 100, 100)
    mininet.ns3.setPosition(ap1, 200, 100, 100)
    mininet.ns3.setPosition(ap2, 300, 100, 100)

    net.addLink(sw0, ap0)
    net.addLink(sw0, ap1)
    net.addLink(sw0, ap2)

    net.start()
    mininet.ns3.start()

    print(mininet.ns3.getPosition(ap0))

    CLI(net)

    mininet.ns3.stop()
    mininet.ns3.clear()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    staticEventNet()
