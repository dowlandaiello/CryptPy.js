<<<<<<< HEAD
# this is the way python packages work
from bot.bot import Bot
from bot.bot import ImportTest
import getpass


ImportTest()

test_bot = Bot(
  "192.168.1.14",
  "bolt",
  getpass.getpass("pwd: ")
)

ifconfig = test_bot.send_command("ifconfig")
print(type(ifconfig))
=======
Bot("192.168.")
>>>>>>> c2c14a5ca0a974df9c1bcb67f6f64a878405152b

print(ifconfig)