from datetime import date
import csv
import os

class FileHandle:

	### Variables ###
	# jsonElement
    # FileName    

    ### Constructors ###
    def __init__(self):
        pass

    def __init__(self, jsonElement):
        self.jsonElement = jsonElement
        #Relative Path
        self.pathFile = os.getcwd() + '/storage/'   
        #Generate FileName
        idStr = str(jsonElement['id'])        
        self.fileName = date.today().strftime("%Y_%m_%d") + '_' + idStr + '.csv'


    ### Setters and Getter ###
    def SetPathFile(self,pathFile):
       self.pathFile = pathFile

    def SetFileName(self,fileName):
       self.fileName = fileName

    def GetFileName(self):
    	return self.fileName

    ### Methods ###

    def JSONElementtoCSVFile(self):        
        csv_file = self.pathFile + self.fileName

        with open(csv_file, 'w') as f:
            w = csv.DictWriter(f, self.jsonElement.keys())
            w.writeheader()
            w.writerow(self.jsonElement)

