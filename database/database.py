try:
    import cPickle as pickle
except ImportError:
    import pickle
from common import commonio
from common import common
from bot import bot

class Database:
    def __init__(self, serverAddr):
        self.Bots = [] # Init empty array
        common.RemoteAddr = serverAddr # Set serveraddr

    # Write self to memory
    def WriteToMemory(self):
        print('-- INFO -- attempting to write db to memory')
        try:
            commonio.WriteToMemory(self.Bots, "database.hax")
        except Exception as e: # account for exception
            print('-- ERROR -- found error while writing to memory: '+str(e))
    
    # Read from memory to self
    def ReadFromMemory(self):
        try:
            with open("database.hax", "rb") as f: # Get file reference
                dump = pickle.load(f) # Load
                self.Bots = dump # Set read dump to self
        except Exception as e: # account for exception
            print(e)