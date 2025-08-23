#!/usr/bin/env python3

import nfc
import sys
import subprocess
import base64

def decode(encoded, key):
    data = base64.b64decode(encoded)
    result = []
    for i, byte in enumerate(data):
        result.append(chr(byte ^ ord(key[i % len(key)])))
    return "".join(result)

with open("/home/gareth/scripts/nfc/key.txt", "r") as f:
    key = f.read().strip()

def on_connect(tag):
    if tag.ndef:
        text = tag.ndef.records[0].text
        decoded = decode(text, key)
        subprocess.run(["xdotool", "type", decoded])
        subprocess.run(["xdotool", "key", "Return"])
    return True

with nfc.ContactlessFrontend('usb') as clf:
    while True:
        clf.connect(rdwr={'on-connect': on_connect})