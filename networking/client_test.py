from networking import client # Import client
from bot import bot # Import bot
import getpass

test_bot = bot.Bot(
    '192.168.1.14',
    getpass.getuser(),
    getpass.getpass("pwd: ")
)

client = client.Client(test_bot) # Init and register client