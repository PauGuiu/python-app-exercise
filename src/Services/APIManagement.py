import requests

class APIManagement:

	### Variables ###
	# url API

    ### Constructors ###
    def __init__(self):
        pass

    def __init__(self, url):
        self.url = url

    ### Setters and Getters###
    def SetURL(self,url):
    	self.url = url

    def GetURL(self):
    	print('URL: ' + self.url)

    ### Methods ###
    def GetInfo(self):
        r = requests.get(self.url)
        return r.json()