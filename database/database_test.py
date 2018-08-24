from database import database

def TestWriteToMemory():
    db = database.Database()

    db.WriteToMemory()

TestWriteToMemory()