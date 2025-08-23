# nfc-implant-login

A Python project for using an xNT NFC implant to login to sudo commands, or any other software, on Linux systems. Also works with NFC cards, tags, or other NFC devices.

It basically reads a stored encoded password, then types it out and presses return (enter).

## Files

### keygen.py
Generates a unique `key.txt` file used for encoding and decoding passwords on the NFC device.

### encode.py
Usage: `./encode.py <string>`

Encodes a password string that can be stored on your NFC device.

### decode.py
Usage: `./decode.py <string>`

Decodes an encoded password string. Optional verification step.

### nfc_app.py
Main application that should be launched on system login. Listens for NFC scans, decodes the stored string, and automatically types the password and presses enter.

## Setup

1. Run `keygen.py` to generate your encryption key
2. Use `encode.py` to encode your password  
3. Store the encoded string on your NFC implant
4. Set `nfc_app.py` to run on system startup
5. Scan your implant when prompted for sudo authentication

## Requirements

- Linux system
- Python 3.x
- NFC reader hardware (Reccomend ACR122U)
- xNT NFC implant (or any NFC card/tag)