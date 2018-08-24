from database import database
import ipgetter

class Server:
    def __init__(self):
        ip = ipgetter.myip()

        databaseReference = database.Database(ip)
        try:
            databaseReference.ReadFromMemory()
        except Exception as e:
            databaseReference.WriteToMemory()

        self.databaseReference = databaseReference