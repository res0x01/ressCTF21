#!/usr/bin/python3
import string
import struct
import random

with open("flag.txt", "r") as f:
    FLAG = f.read().strip()

const_max_num = 1000

for i in FLAG:
    for j in range(random.randrange(0,const_max_num)):
        print(chr(128+random.randrange(0,const_max_num)),end="")
    print(i,end="")

