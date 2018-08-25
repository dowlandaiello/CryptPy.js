from database import database
from common.commondefs import true
from bot import bot
from common import common
import ipgetter
import socket
import sys
import pprint

class Server:
    def __init__(self):
        ip = ipgetter.myip() # Get external IP

        databaseReference = database.Database(ip) # Init db
        try:
            databaseReference.ReadFromMemory() # Attempt to read from memory
        except Exception:
            databaseReference.WriteToMemory() # Write new to memory if nonexistent

        self.databaseReference = databaseReference # set db ref to init db

        self.startServer() # start server
    
    def startServer(self):
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
            finally:
                connection.close() # Close connection

                print('-- CONNECTION -- connection closed') # Log closed connection


