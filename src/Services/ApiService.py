from sys import stderr
from .APIManagement import APIManagement
from .FileHandle import FileHandle

#The aim of this class is 

class ApiService:

    def __init__(self):
        pass

    def run(self):
        print('Running ApiService\n', file=stderr)

        # TODO: follow README.md instructions        
        #API URL
        url = 'https://jsonplaceholder.typicode.com/todos/'

        try:
            # Get Info from API and create a JSON object
            print('Get TODOS from the API...')
            API = APIManagement(url)        
            info = API.GetInfo()        
            print('Success\n')
        
            # Extract JSON Elements and Generate CSV Files
            print('Extracting data and generating files...\n')
            for jsonElement in info:            
                handle = FileHandle(jsonElement)
                handle.JSONElementtoCSVFile()
                print('File Generated succesfully: ' + handle.GetFileName())

            #Finished
            print('\nApiService Finished.')
        
        except IOError:
                #Handle I/O Exceptions
                print("An I/O exception occurred while creating a file.")
        except:
                #Handle Unknown Exceptions
                print("Some exception occurred.")      
       
