from sys import stderr
from .APIManagement import APIManagement
from .FileHandle import FileHandle


class ApiService:

    def __init__(self):
        pass

    def run(self):
        print('Running ApiService\n', file=stderr)

        # TODO: follow README.md instructions        
        #API URL
        url = 'https://jsonplaceholder.typicode.com/todos/'

        try:
            # Get Info
            print('Get TODOS from the API...')
            API = APIManagement(url)        
            info = API.GetInfo()        
            print('Success\n')
        
            # Extracr Info and Generate File
            print('Extracting data and generating files...\n')
            for jsonElement in info:            
                handle = FileHandle(jsonElement)
                handle.JSONElementtoCSVFile()
                print('File Generated succesfully: ' + handle.GetFileName())

            #Finished
            print('\nApiService Finished.')
        
        except IOError:
                print("An I/O exception occurred while creating a file.")
        except:
                print("Some exception occurred.")      
       
