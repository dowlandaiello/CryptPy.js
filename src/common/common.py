from common.commondefs import none
from common.commondefs import false
import sys, os
from src.portforwardlib import forwardPort as forwardNetPort

RemoteAddr = "108.27.18.36" # Add server address

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

    forwardNetPort(port, port, none, none, false, 'TCP', 0, 'CryptPy.js', false) # Forward port

def forwardPortStandard():
    port = 3000

    forwardNetPort(port, port, none, none, false, 'TCP', 0, 'CryptPy.js', false) # Forward port