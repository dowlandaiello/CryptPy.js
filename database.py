from bot import bot
import common

class Database():
    Bots = [bot.Bot] # Init empty array


    # Write self to memory
    def WriteToMemory():
        try:
            common.WriteToMemory(self, "database.hax")
        except Exception as e: # account for exception
            print(e)
    
    # Read from memory to self
    def ReadFromMemory():
        with open("database.hax", "rb") as f: # Get file reference
            dump = pickle.load(f) # Load
            self = dump # Set read dump to self