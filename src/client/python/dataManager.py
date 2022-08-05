class dataManager():
    def __init__(self, fileName):
        self.Headers = ["batch_id", "timestamp", "reading1","reading2","reading3","reading4","reading5","reading6","reading7","reading8","reading9","reading10",]
        self.fileName = fileName
        self.fileData = []
        self.adjustmentsMade = [0] #list of integer values that stores the code indicating adjustments made - only 0 indicate no change
                                   #list used as multiple adjustments can be made to the same data
    
    def checkData(self):
        self.checkHeaders()
        self.checkColumnCount()
        self.checkFloats()
        self.checkFilenameFormat()
        self.checkNotNil()
        
    def checkHeaders(self):
        for header in self.Headers:
            if !(header)

    def checkColumnCount(self):
        return

    def checkFloats(self):
        return

    def checkFilenameFormat(self):
        return

    def checkNotNil(self):
        return

    def correctHeaders(self):
        self.adjustmentsMade.append(1) #indicates that 
        return

    def correctFilename(self):
        self.adjustmentsMade.append(2)
        return