from database import database
from common.commondefs import true
from bot import bot
import ipgetter
import socket
import sys

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

        sock.bind(('localhost', 3000)) # Bind socket to server address

        sock.listen(1) # Listen

        while true:
            print('waiting for connection') # Log begin
            connection, client_address = sock.accept() # Accept connection

            try:
                print('connection from bot '+client_address) # Log accepted connection

                total_data = [] # Init data buffer

                while true:
                    data = connection.recv(16) # Attempt to read 
                    print('received '+len(data)+' bits of data') # Log received data

                    if data:
                        print('found data')
                        total_data.append(data) # Append data to list
                    else:
                        print('found end of data stream')
                        break # Found end of data stream, break loop
                print(type(total_data[0])) # [Debug] log type of total_data
            finally:
                connection.close()


