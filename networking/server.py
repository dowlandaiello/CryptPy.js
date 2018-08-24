from database import database
from common.commondefs import true
import ipgetter
import socket
import sys

class Server:
    def __init__(self):
        ip = ipgetter.myip()

        databaseReference = database.Database(ip)
        try:
            databaseReference.ReadFromMemory()
        except Exception:
            databaseReference.WriteToMemory()

        self.databaseReference = databaseReference
        self.ipAddress = ip

        self.startServer()
    
    def startServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = self.ipAddress

        sock.bind(server_address)

        sock.listen(1)

        while true:
            print('waiting for connection')
            connection, client_address = sock.accept()

            try:
                print('connection from bot '+client_address)

                total_data = []

                while true:
                    data = connection.recv(16)
                    print('received '+len(data)+' bits of data')

                    if data:
                        print('found data')
                        total_data.append(data)
                    else:
                        print('found end of data stream')
                        break
            finally:
                connection.close()


