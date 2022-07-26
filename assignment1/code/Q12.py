#!/usr/bin/env python
#coding -*- utf:8 -*-
import math
import random

import binascii
# convert string to integer using
def string_to_int(string):
    return int.from_bytes(binascii.a2b_qp(string),byteorder='big')
# convert into back to string
def int_to_string(number):
    bin = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')
    return binascii.b2a_qp(bin).decode("utf-8")

n = string_to_int('0x9B51C20306EDE535C8FCAADBC3F3515E52A0D005703DD449BEC66B23E2932313')
p = string_to_int('0xC5A047A7C52ED3A2875F7D76C47B555F')
q = string_to_int('0xC93268355C09197BBF1659B5522FFACD')
e = string_to_int('0x010001')
d = string_to_int('0x0D067636BAC6088AD2281E4BFFCACFEFEF9BC1A69FB9E701063DFBAAB436E4C1')
cipher = string_to_int('0x13121ff7d7be2301a4db5801d6d142e9bb3fbef7f4c73c14f647d5f43ebc8db3')

def quick_algorithm(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans

plaintext = quick_algorithm(cipher,d,n)
print(plaintext)