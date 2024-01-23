import os
import simplejson
import json
import requests


class Elsevier_rest():
    
    def __init__(self, *args, **kwargs):
        
        self.baseurl = "https://api.elsevier.com/content/search/sciencedirect"
        self.apiKey = os.environ.get('elsevier-api-key')
        
    def basicQuery(self, q):
        
        url = self.url
        
        params = {
            q: q,
            apiKey: self.apiKey,
        }
        
        response = requests.request("GET", url, params=params)
        
        data = response.json()
        
        # process through the json to get what we want to show
        
        # return context
        
            
        