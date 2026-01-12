# NetGecko - Wii Network Debug Logger
# Copyright (c) 2026 GatoWare
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Any modifications must clearly state that they were modified
# and must reference the original repository:
# https://github.com/oxyzin/netgecko

import socket
from datetime import datetime

s = socket.socket()
s.bind(("0.0.0.0", 4000))
s.listen(1)
version = "1.0"
print(f"NetGecko {version}")
print("Waiting for Wii...")

conn, _ = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break

    msg = data.decode()

    now = datetime.now()
    timestamp = f"({now.hour:02d}:{now.minute:02d}:{now.second:02d}) "
    
    # prints line by line to avoid confusion
    for line in msg.splitlines(True):
        print(timestamp + line, end="")
