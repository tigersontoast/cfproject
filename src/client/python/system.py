from fileManager import fileManager
from dataManager import dataManager
from art import *
from datetime import datetime
import ftplib


class system():
    def __init__(self):
        self.startupPrompt() #print out startup prompt
        self.startupFTP()
        self.getRequestedDate()
        self.dataManager = dataManager("peekaboo")
        self.fileManager = fileManager(self.dataManager, self.serverSession)

    def getRequestedDate(self):
        print("Enter the day for which you would like the date (DD/MM/YYYY)")
        validDate = False
        while not(validDate):
            date = input("")
            if len(date) != 10: #must be 8 characters
                print("Please provide a valid date in format DD/MM/YYYY")
            try:
                dateTimeObj = datetime.strptime(date, '%d/%m/%y')
            except:
                print("Date invalid")
        



    def startupPrompt(self):
        art = text2art("mediKeep") #ascii art of the name
        print(art)
        print( "\u2695" * 52)
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #print current date and time
        print("-" * 52)
        print(dt_string)
        print("-" * 52 )
    
    def startupFTP(self):
        self.serverSession = ftplib.FTP()
        self.serverSession.connect('127.0.0.1', 2121) #create a session, connecting to the FTP server
        
        

System = system()
