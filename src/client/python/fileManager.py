####TO DO####

class fileManager():
    def __init__(self, dataManager, serverSession):
        serverSession.login("user", "12345")
        serverSession.cwd("files")
        serverSession.dir()

    def fetch(fileName):
        pass

    def read():
        pass

    def write():
        pass

    def move(fromString, toString):
        pass

    def log(message):
        pass