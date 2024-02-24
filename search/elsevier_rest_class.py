import os
import simplejson
import json
import requests
from datetime import datetime

'''
This class is used to access the upstream elsevier API service.
'''
class Elsevier_rest():
    
    '''
    Runs at instantiation, this function establishes the baseurl 
    and pulls in the API key for later use
    '''
    def __init__(self, *args, **kwargs):
        
        # TODO: Move hard coded URL to .env file
        self.baseurl = "https://api.elsevier.com/content/search/sciencedirect"
        self.apiKey = os.environ.get('elsevier_api_key')
        
    '''
    This function is to call the upstream elseiver API service. 
    The service is paginated, with a default of 25 results returned, starting with the 
    first result.
    
    The q parameter represents the search string. It is required.
    The num_pages parameter is used to adjust the number of results returned in a single query. It is optional, the default is 25.
    The start_page parameter is used to determine what number of result to start from. It is optional, the default is 0.
    
    The swagger documentation at '/search/api/swagger-ui' documents the inputs and response expected.
    '''    
    def query(self, q, num_pages=25, start_page=0):
        
        url = self.baseurl
        
        dateFormat = "%Y-%m-%dT%H:%M:%S.%fZ"        
            
        params = {
            'query': q,
            'count': num_pages,
            'start': start_page,
            'apiKey': self.apiKey,
        }
        
        response = requests.request("GET", url, params=params)
        
        context = {
            "status": response.status_code,
        }
        
        if response.status_code == 200:
        
            data = response.json()
        
            totalResults = int(data['search-results']['opensearch:totalResults'])
            currentPage = int(data['search-results']['opensearch:startIndex'])
            pageSize = int(data['search-results']['opensearch:itemsPerPage'])
            entries = data['search-results']['entry']
        
            resultRows = []
        
            if int(totalResults) != 0:
                for entry in entries:
            
                    loadDateTime = datetime.strptime(entry['load-date'], dateFormat)
                    
                    try:
                        row = {
                            "identifier": entry['dc:identifier'],
                            "url": entry['prism:url'],
                            "title": entry['dc:title'],
                            "creator": entry['dc:creator'],
                            "publication": entry['prism:publicationName'],
                            "loadDate": loadDateTime.strftime('%y-%m-%d'),
                        } 
            
                        resultRows.append(row)
                    except KeyError:
                        continue    
            
                context = {
                    'status': response.status_code,
                    'results': totalResults,
                    'currentPage': currentPage,
                    'pageSize': pageSize,
                    'resultRows': resultRows,
                }
        return context
        
        
        