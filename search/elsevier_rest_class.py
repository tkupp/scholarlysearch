import os
import simplejson
import json
import requests
from datetime import datetime


class Elsevier_rest():
    
    def __init__(self, *args, **kwargs):
        
        # TODO: Move hard coded URL to .env file
        self.baseurl = "https://api.elsevier.com/content/search/sciencedirect"
        self.apiKey = os.environ.get('elsevier_api_key')
        
        
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
        
        
        