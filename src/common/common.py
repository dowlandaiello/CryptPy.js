from src.common.commondefs import none
from src.common.commondefs import false
from src.common.portforwardlib import forwardPort as forwardNetPort # Runs anyway
import sys, os

RemoteAddr = '104.248.4.185' # Add server address

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
