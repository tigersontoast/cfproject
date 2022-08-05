import socket
import sys
import time
import os
import struct

print("\nWelcome to the FTP server.\n\nTo get started, connect a client")
TCP_IP = "127.0.0.1"
TCP_PORT = 21
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print("\nConnected to by address: {}".format(addr))


def list_files():
    print("Listing files...")
    listing = os.listdir(os.getcwd())
    conn.send(struct.pack("i", len(listing)))
    total_directory_size = 0
    for i in listing:
        conn.send(struct.pack("i", sys.getsizeof(i)))
        conn.send(i)
        conn.send(struct.pack("i", os.path.getsize(i)))
        total_directory_size += os.path.getsize(i)
        conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("i", total_directory_size))
    conn.recv(BUFFER_SIZE)
    print("Successfully sent file listing")
    return

def main():
    while True:
        data = conn.recv(BUFFER_SIZE)
        data = data.decode(encoding='utf_8', errors='strict')
        if data == "LIST":
            print("LIST")
            list_files()
        elif data == "QUIT":
            print("QUIT")
            quit()
        data = None

def quit():
    conn.send(str.encode("1"))
    conn.close()
    s.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

if __name__ == '__main__':
    main()