#Code taken from UCT-EE-OCW/EEE3096S-2021/WorkPackage6

import socket
import sys
import time

HOST = '0.0.0.0'  # Symbolic name meaning all available interfaces
PORT = 5003  # Arbitrary non-privileged port
s = None
f = open("/data/sensorlog.txt", "w+")

#try to make socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as msg:
    s = None
try:
    s.bind((HOST,PORT))
    s.listen(1)
except OSError as msg:
    s.close()
    s = None

if s is None:
    print('could not open socket')
    f.write("Could not open socket\n")
    f.close()
    sys.exit(1)


conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    f.write("Connected by" + str(addr) + "\n")
    f.flush()
    while True:
        data = conn.recv(1024)
        data = data.decode()
        print('Received', repr(data))
        #added formatting to data
        data = data + '\n'
        #write data to sensorlog.txt
        f.write(data)
        f.flush()
        #added wait to help with Received data handling
        time.sleep(1)
        if not data: break
