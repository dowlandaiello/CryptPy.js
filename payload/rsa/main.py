from key import Key
from encrypt import Encrypt

def new_key():
    key = Key()
    key.new_key(4096)


def encrypt():
    Encrypt(
        [
            "test/test1",
            "test/test2"
        ],
        "3b4e434"
    )
# new_key()
encrypt()