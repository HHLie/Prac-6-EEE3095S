import socket
import sys
import time

HOST = None  # Symbolic name meaning all available interfaces
PORT = 5003  # Arbitrary non-privileged port
s = None
f = open("/data/sensorlog.txt", "w+")
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    f.write("Could not open socket\n")
    f.close()
    sys.exit(1)


connected = False
while not connected:
    try:
        conn, addr = s.accept()
        connected = True
    except Exception as e:
        pass

#conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    f.write("Connected by" + str(addr) + "\n")
    f.flush()
    while True:
        data = conn.recv(1024)
        data = data.decode()
        print('Received', repr(data))
        data = data + '\n'
        f.write(data)
        f.flush()
        time.sleep(1)
        if not data: break
