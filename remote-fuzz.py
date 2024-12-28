import socket
from struct import pack

IP = "localhost"
port = 1337

def fuzz():
    try:
        for i in range(0,10000,500):
            buffer = b"A"*i
            print("Fuzzing %s bytes" % i)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, port))
            s.send(buffer)
            breakpoint() # script asks if app is crashed, etc.
            s.close()
    except:
        print("Could not establish a connection")