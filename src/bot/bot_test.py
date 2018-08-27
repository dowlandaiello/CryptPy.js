from bot import bot

bot.ImportTest() # Test importable

test_bot = bot.Bot(
    '192.168.1.14',
)

ifconfig = test_bot.send_command("ifconfig") # Send command

print(ifconfig) # Log output
