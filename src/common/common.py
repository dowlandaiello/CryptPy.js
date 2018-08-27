from common.commondefs import none
import sys, os
import miniupnpc

RemoteAddr = "localhost" # Add server address

# Disable calls to print()
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Restore calls to print()
def enablePrint():
    sys.stdout = sys.__stdout__

# Attempts to forward given port
def forwardPort(port):
    if port is none or port == 0:
        port = 3000

    upnp = miniupnpc.UPnP() # Init UPnP

    upnp.discover() # Discover devices

    upnp.selectigd() # Select device

    upnp.addportmapping(port, 'TCP', upnp.lanaddr, port, 'CryptPy.js', '') # Forward port

def forwardPortStandard():
    port = 3000
    
    upnp = miniupnpc.UPnP() # Init UPnP

    upnp.discover() # Discover devices

    upnp.selectigd() # Select device

    upnp.addportmapping(port, 'TCP', upnp.lanaddr, port, 'CryptPy.js', '') # Forward port