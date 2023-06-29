#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from zlib import decompress
import os

def decrypt_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        
    aes_key = data[:16]
    aes_obj = AES.new(aes_key, AES.MODE_CBC, iv = data[16:32])
    dec_dat = unpad(aes_obj.decrypt(data[32:]), AES.block_size)
    
    with open(filename[:-10], 'wb') as f:
        f.write(decompress(dec_dat))

if __name__ == '__main__':
    path = 'target'
    for file_name in os.listdir(path):
        decrypt_file(os.path.join(path, file_name))