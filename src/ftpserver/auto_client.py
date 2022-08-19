import ftplib
server = ftplib.FTP()
server.connect('127.0.0.1', 2121)

server.login("user", "12345")
server.dir()