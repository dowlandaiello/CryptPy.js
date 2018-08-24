import bot
try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

class Database():
    Nodes = [bot.bot.Bot()] # Init empty array


    # Write self to memory
    def WriteToMemory():
        with open("database.hax", "wb") as f: # Init file reference
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL) # Dump to file
    
    # Read from memory to self
    def ReadFromMemory():
        with open("database.hax", "rb") as f: # Get file reference
            dump = pickle.load(f) # Load
            self = dump # Set read dump to self