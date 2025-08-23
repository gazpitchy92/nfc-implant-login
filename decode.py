#!/usr/bin/env python3
import sys
import base64

def decode(encoded, key):
    data = base64.b64decode(encoded)
    result = []
    for i, byte in enumerate(data):
        result.append(chr(byte ^ ord(key[i % len(key)])))
    return "".join(result)

if len(sys.argv) < 2:
    print("Usage: ./decode.py <encoded_string>")
    sys.exit(1)

with open("./key.txt", "r") as f:
    key = f.read().strip()

input_text = sys.argv[1]
print(decode(input_text, key))