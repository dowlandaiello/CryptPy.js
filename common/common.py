import sys, os

RemoteAddr = "localhost" # Add server address

# Disable calls to print()
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Restore calls to print()
def enablePrint():
    sys.stdout = sys.__stdout__