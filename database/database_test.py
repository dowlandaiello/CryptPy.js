from database import database

# TestWriteToMemory - test functionality of writetomemory method
def TestWriteToMemory():
    db = database.Database('192.168.1.14') # Init new database

    db.WriteToMemory() # Write Database to memory

# TestReadFromMemory - test functionality of readfrommemory method
def TestReadFromMemory():
    db = database.Database('192.168.1.14') # Init new database

    db.WriteToMemory() # Write Database to memory

    db.ReadFromMemory() # Attempt to read database from memory

TestWriteToMemory() # Run write test
TestReadFromMemory() # Run read test