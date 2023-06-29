#!/usr/bin/python3

from pwn import xor

flag = b"debug_debug_n_debug_for_the_key_a53dfa"
secret = b"151235"

# print([x for x in secret])
a = [x for x in xor(flag, secret)]
print(a)
print(len(a))
print(xor(flag, secret).decode())

print(xor(a, secret))
