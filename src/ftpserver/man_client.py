import socket
import sys
import os
import struct
from ftplib import FTP

TCP_IP = "127.0.0.1" 
TCP_PORT = 21
BUFFER_SIZE = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((TCP_IP, TCP_PORT))

while True:
    prompt = input("\nEnter a command: ")
    if prompt[:4].upper() == "QUIT":
        quit()
        break
    elif prompt[:4].upper() == "LIST":
        break
    else:
        print("Command not recognised; please try again")

def quit():
    s.send("QUIT")
    s.recv(BUFFER_SIZE)
    s.close()
    print("Server connection ended")
    return


def  list_files():
    print("Requesting files... \n")
    try:
        s.send("LIST")
    except:
        print("could not connect")
        return
    try:
        number_of_files = struct.unpack("i", s.recv(4))[0]
        for i in range(int(number_of_files)):
            file_name_size = struct.unpack("i", s.recv(4))[0]
            file_name = s.recv(file_name_size)
            file_size = struct.unpack("i", s.recv(4))[0]
            print("\t{} - {}b").format(file_name, file_size)
            s.send(1)
            total_directory_size = struct.unpack("i", s.recv(4))[0]
            print("Total directory size: {}b").format(total_directory_size)
    except:
        print("could nto retrieve listing")
        return
    try:
        s.send(1)
        return
    except:
        print("could not get server confirmation")
        return