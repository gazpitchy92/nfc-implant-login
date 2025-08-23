#!/usr/bin/env fish

pkill -f nfc_app.py

while true
    python ./nfc_app.py
    echo "nfc_app.py crashed or exited, restarting in 5s..."
    sleep 5
end
