from networking import client # Import client
from bot import bot # Import bot

test_bot = bot.Bot(
    '192.168.1.14',
)

client = client.Client(test_bot) # Init and register client