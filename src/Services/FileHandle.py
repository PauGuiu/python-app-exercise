from datetime import date
import csv
import os

#Note:The Pandas library has not been chosen for efficiency reasons. I usually use it for the treatment of more extensive data. 

#Class designed to handle JSON information and generate CSV Files.

class FileHandle:

	### Variables ###
	# jsonElement
    # FileName    

    ### Constructors ###
    def __init__(self):
        pass

    #Initialize local variables generating relative path file and filename.
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

    #JSONElementtoCSVFile: Generate CSV files with JSON information.
    #Input: Void
    #Output: Void    
    def JSONElementtoCSVFile(self):        
        csv_file = self.pathFile + self.fileName

        with open(csv_file, 'w') as f:
            w = csv.DictWriter(f, self.jsonElement.keys())
            w.writeheader()
            w.writerow(self.jsonElement)



