import os
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    #need to change directory
    logging.basicConfig(filename='logging/ftp.log', level=logging.INFO)

    # Instantiate FTP server class and listen on 127.0.0.1:2121
    address = ('127.0.0.1', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    print("Starting FTP server...")
    # start ftp server
    server.serve_forever()
    

if __name__ == '__main__':
    main()