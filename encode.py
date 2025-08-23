#!/usr/bin/env python3
import sys
import base64

def encode(text, key):
    result = bytearray()
    for i, char in enumerate(text):
        result.append(ord(char) ^ ord(key[i % len(key)]))
    return base64.b64encode(result).decode()

if len(sys.argv) < 2:
    print("Usage: ./encode.py <string>")
    sys.exit(1)

with open("./key.txt", "r") as f:
    key = f.read().strip()

input_text = sys.argv[1]
print(encode(input_text, key))