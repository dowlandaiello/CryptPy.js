from common import common
from common import commonio
from bot import bot
import socket
import sys
try:
    import cPickle as pickle
except ImportError:
    import pickle

class Client:
    def __init__(self, botRef: bot.Bot):
        self.bot = bot.Bot
        self.hostNode = common.RemoteAddr # Set host node addr for persistency
        self.bot.user = botRef.user # Set bot user for persistency
        self.bot.password = botRef.password # Set pass for persistency
        self.bot.host = botRef.host # Set host for persistency
        self.bot.session = botRef.session # Set session for persistency

        self.RegisterClient() # Register client
    
    def RegisterClient(self):
        if self.hostNode == '': # Check for nil host node
            return 'invalid host node' # Return error
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Init socket

        serialized = commonio.ToBytes(self.bot) # Attempt to serialize

        sock.sendall(serialized) # Send self bot reference
        sock.close() # Close socket