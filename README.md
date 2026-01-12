# NetGecko

NetGecko is a debugger for the Nintendo Wii that works over the network.  
It allows you to send debug logs from your homebrew directly to your PC using Wi-Fi or Ethernet, acting as a modern replacement for the classic USB Gecko.

---

## Features

- Real-time logging over TCP
- Works with Wi-Fi and Ethernet
- Header-only library
- Extremely lightweight and simple

---

## How it works

NetGecko opens a TCP connection from the Wii to your PC.  
All debug messages are sent through this connection and displayed by a small Python server.

---

## PC Side (Server)

Run the debug server:

```bash
python3 -u server.py | tee net.log
```

## Wii Side (Usage)

Include the header:
```c
#include "netgecko.h"
```

Initialize the connection:
```c
NG_Init("192.168.X.XX"); // Server local IP
```

Send a log:
```c
NG_Log("Hello World!\n");
```

When finished, close the connection:
```c
NG_Close();
```
## License
Apache License 2.0

You are free to:

Use  
Modify  
Distribute  

As long as you:

Keep credits to the original author  
Reference the original repository  
State modifications if you change the code  

## Credits
Created by GatoWare (OxyZin)
