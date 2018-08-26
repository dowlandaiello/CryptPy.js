from pexpect import pxssh
from common.commondefs import false
from common.commondefs import none
import marshal
import sys
import os
import requests
import simplejson as json

class ImportTest:
    def __init__(self):
        print("imported successfully") # Log success
class Bot:
    # init class instance
    def __init__(self, host, user, password):
        self.host = host # Fetch and store host reference
        self.user = user # Fetch and store username
        self.password = password # Fetch and store user password
        self.rest()

    # secure shell into bot
    def ssh(self):
        try:
            bot = pxssh.pxssh() # Open ssh client instance
            bot.login(self.host, self.user, self.password, auto_prompt_reset=false) # Login to ssh terminal
            return bot
        except Exception as e: # Account for exceptions
            print('connection failure') # Handle exception
            print(e) # Print exception

    # open rest gateway to bot
    def rest(self):
        try:
            os.system('rest-shell --server localhost:3000')
        except Exception as e:
            print('connection failure')
            print(e)

    # sending a command to the client
    def send_command(self, command):
        url = "http://"+self.host+":3000" # Get addr

        data = {'command': command}
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

        return r.json() # Return response

    # dump to bytes
    def to_bytes(self):
        return marshal.dumps(self)

    # dump params to bytes
    def params_to_bytes(self):
        arr = [self.host, self.user, self.password]
        return marshal.dumps(arr)

    # read from bytes
    def from_bytes(self, b):
        self = marshal.loads(b)

def byte_params_to_bot(b):
    arrVal = marshal.loads(b)
    return Bot(arrVal[0], arrVal[1], arrVal[2])