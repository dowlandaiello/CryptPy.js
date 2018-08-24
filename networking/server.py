from database import database
import ipgetter

class Server:
    def __init__(self):
        ip = ipgetter.myip()

        databaseReference = database.Database(ip)
        databaseReference.ReadFromMemory()

        self.databaseReference = databaseReference