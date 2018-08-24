try:
    import cPickle as pickle
except ImportError:
    import pickle
from common import commonio
from common import common
from bot import bot

class Database:
    def __init__(self, serverAddr):
        self.Bots = [bot.Bot] # Init empty array
        common.RemoteAddr = serverAddr


    # Write self to memory
    def WriteToMemory(self):
        try:
            commonio.WriteToMemory(self, "database.hax")
        except Exception as e: # account for exception
            print(e)
    
    # Read from memory to self
    def ReadFromMemory(self):
        try:
            with open("database.hax", "rb") as f: # Get file reference
                dump = pickle.load(f) # Load
                self.Bots = dump.Bots # Set read dump to self
        except Exception as e: # account for exception
            print(e)