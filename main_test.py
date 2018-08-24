import bot.bot

import getpass

bot = bot.bot

bot.ImportTest()

test_bot = bot.Bot(
  "192.168.1.14",
  "bolt",
  getpass.getpass("pwd: ")
)

ifconfig = test_bot.send_command("ifconfig")
print(type(ifconfig))

print(ifconfig)
