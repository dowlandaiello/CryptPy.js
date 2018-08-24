from pexpect import pxssh

class ImportTest:
    def __init__(self):
        print("imported successfully") # Log success
class Bot:
    # init class instance
    def __init__(self, host, user, password):
        self.host = host # Fetch and store host reference
        self.user = user # Fetch and store username
        self.password = password # Fetch and store user password
        self.session = self.ssh() # Fetch and store ssh session

    # secure shell into bot
    def ssh(self):
        try:
            bot = pxssh.pxssh() # Open ssh client instance
            bot.login(self.host, self.user, self.password, auto_prompt_reset=False) # Login to ssh terminal
            return bot
        except Exception as e: # Account for exceptions
            print('connection failure') # Handle exception
            print(e) # Print exception

    # sending a command to the client
    def send_command(self, command):
        self.session.sendline(command)
        self.session.prompt() # match the prompt
        return self.session.before # everything before the prompt