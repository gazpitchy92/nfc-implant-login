#!/usr/bin/env python3
import os

key_length = 32
key = os.urandom(key_length).hex()

with open("./key.txt", "w") as f:
    f.write(key)

print(f"Generated key ({key_length*2} hex chars) saved to key.txt")