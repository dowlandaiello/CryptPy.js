from database import database
from common.commondefs import true
from common import common
from bot import bot
from command import command
import requests
import urllib3
import ipgetter
import socket
import sys
import pprint
import threading
import time

class Server:
    def __init__(self, flags):
        ip = ipgetter.myip() # Get external IP

        self.databaseReference = database.Database(ip) # Init db
        try:
            self.databaseReference.ReadFromMemory() # Attempt to read from memory
        except Exception as e:
            print(e) # Log found exception
            self.databaseReference.WriteToMemory() # Write new to memory if nonexistent

        self.startServer(flags) # start server
    
    def startServer(self, flags):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        serverThread = threading.Thread(target=self.startServerOnly) # Init server thread
        serverThread.daemon = true # Run as background thread
        serverThread.start() # Start server thread

        time.sleep(0.5) # No clue

        if "terminal" in flags: # Check for terminal flag
            self.startTerminal() # Start terminal

    def startServerOnly(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Init socket

        server_address = ('localhost', 3000)

        sock.bind(server_address) # Bind socket to server address

        print('\n-- INFO -- starting with address '+server_address[0]+':'+str(server_address[1]))

        sock.listen(1) # Listen

        while true:
            print('\nwaiting for connection...\n') # Log begin
            connection, client_address = sock.accept() # Accept connection

            try:
                print('-- CONNECTION-- found new connection from bot '+client_address[0]) # Log accepted connection

                data = connection.recv(4096) # Read from connection

                print('received '+str(len(data))+' bits of data') # Log received data

                botRef = bot.byte_params_to_bot(data) # Init bot from data

                print('found bot with address '+botRef.host) # Log found bot

                self.databaseReference.Bots.append(botRef) # Append found bot

                self.databaseReference.WriteToMemory() # Write db to memory
            finally:
                connection.close() # Close connection

                print('-- CONNECTION -- connection closed') # Log closed connection

    # Start terminal
    def startTerminal(self):
        while true:
            userInput = input('> ') # Fetch input

            commandThread = threading.Thread(target=command.command_bots(userInput, self.databaseReference.Bots)) # Init command thread
            commandThread.daemon = true # Run as background thread
            commandThread.start() # Start command thread
            continue




