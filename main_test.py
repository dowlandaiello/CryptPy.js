from bot.bot import Bot, ImportTest

import getpass


ImportTest()

test_bot = Bot(
  "192.168.1.14",
  "bolt",
  getpass.getpass("pwd: ")
)

ifconfig = test_bot.send_command("ifconfig")
print(type(ifconfig))

print(ifconfig)

