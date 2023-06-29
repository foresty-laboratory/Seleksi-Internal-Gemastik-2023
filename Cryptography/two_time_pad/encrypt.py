from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

KEY = os.urandom(16)
FLAG = open('flag.txt', 'rb').read()
MSG = b"AES is secure encryption right? I'm sure no one will be able to decrypt this!"

def encrib(text, key):
    ctr = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(text).hex()

FLAG_ENC = encrib(FLAG, KEY)
MSG_ENC = encrib(MSG, KEY)

OUT = open('result.txt', 'w')
OUT.write('Flag: ' + FLAG_ENC + '\n')
OUT.write('Message: ' + MSG_ENC)
OUT.close()
