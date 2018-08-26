import sys, os
import upnpclient

RemoteAddr = "localhost" # Add server address

# Disable calls to print()
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Restore calls to print()
def enablePrint():
    sys.stdout = sys.__stdout__

# Attempts to forward given port
def forwardPort(port):
    devices = upnpclient.discover() # Get devices
    devices[0].WANIPConn1.AddPortMapping(port)