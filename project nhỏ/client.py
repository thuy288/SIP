  GNU nano 2.5.3              File: client.py                                   

#!/usr/bin/env python3

# Importing libraries
import socket
import sys

# Lets catch the 1st argument as server ip
if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("\n\n Run like \n python3 client.py < serverip address > \n\n")
    exit(1)


# Now we can create socket object
s = socket.socket()

# Lets choose one port and connect to that port
PORT = 9898
                               [ Read 37 lines ]
^G Get Help  ^O Write Out ^W Where Is  ^K Cut Text  ^J Justify   ^C Cur Pos
^X Exit      ^R Read File ^\ Replace   ^U Uncut Text^T To Linter ^_ Go To Line

