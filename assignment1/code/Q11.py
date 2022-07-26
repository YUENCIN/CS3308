import os
import random

byte_list = []
random.seed(2021)

with open("secret2021.enc", "r+", encoding='utf-8', errors='ignore') as f:
    while True:
        byte = f.read(1)
        if not byte:
            continue
        key = random.randrange(255)
        x = key ^ ord(byte)
        print(chr(x))
        byte_list.append(byte)

#print(byte_list)