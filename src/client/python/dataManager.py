from ast import Not
from datetime import datetime

class dataManager():
    HEADERS = ["batch_id", "timestamp", "reading1","reading2","reading3","reading4","reading5","reading6","reading7","reading8","reading9","reading10",] #declare as const - never going to change
    def __init__(self, fileName):
        self.fileName = fileName #store fileName in instance variable
        self.fileData = [[]] #create placeholder for filedata. This variable will be written into by fileManager class
        self.adjustmentsMade = [] #list of string values describing any adjustments made
    
    def checkData(self): #run all necessary checks
        self.checkHeaders()
        self.checkColumnCount()
        self.checkTimeStamps()
        self.checkFloats()
        self.checkFilenameFormat()
        self.checkNotNil()
        
    def checkHeaders(self):
        for headerIndex in range (0, len(self.fileData[0]) -1 ):
            if self.fileData[0][headerIndex] not in dataManager.HEADERS: #if the header in fileData[0] is not a valid header 
                self.correctHeader(headerIndex)                          #then call correctHeader, indicating which index to correct   
        return

    def checkColumnCount(self):
        return

    def checkFloats(self):
        return

    def checkFilenameFormat(self):
        return

    def checkNotNil(self):
        return

    def correctHeaders(self, headerIndex):
        self.incorrectHeaderString = self.fileData[0][headerIndex]
        self.fileData[0][headerIndex] = dataManager.HEADERS[headerIndex]

        self.adjustmentsMade.append(dataManager.getFormattedDateTime() + " corrected header from " + self.incorrectHeaderString + " -> " + dataManager.HEADERS[headerIndex]) #append appropriate message
        return

    def correctFilename(self):
        self.adjustmentsMade.append(2)
        return

    def checkTimeStamps(self):
        return

    @staticmethod #make static method to make accessible to other classes without instantiation
    def getFormattedDateTime():
        dateTimeString = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #get current datetime and format into string DD/MM/YYY HH:MM:SS
        return dateTimeString

