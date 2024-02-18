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
        
        
    def basic_query(self, q):
        
        url = self.baseurl
        
        dateFormat = "%Y-%m-%dT%H:%M:%S.%fZ"    
            
        params = {
            'query': q,
            'apiKey': self.apiKey,
        }
        
        response = requests.request("GET", url, params=params)
        data = response.json()
        
        # Populate variables, proof of concept, this needs significant rework to be fully viable.
        totalResults = data['search-results']['opensearch:totalResults']
        currentPage = data['search-results']['opensearch:startIndex']
        pageSize = data['search-results']['opensearch:itemsPerPage']
        entries = data['search-results']['entry']
        
        
        resultRows = []
        
        if int(totalResults) != 0:
            for entry in entries:
            
                loadDateTime = datetime.strptime(entry['load-date'], dateFormat)
            
                row = {
                    "identifier": entry['dc:identifier'],
                    "url": entry['prism:url'],
                    "title": entry['dc:title'],
                    "creator": entry['dc:creator'],
                    "publication": entry['prism:publicationName'],
                    "loadDate": loadDateTime.strftime('%y-%m-%d'),
                } 
            
                resultRows.append(row)
            
            
            
        context = {
            'results': totalResults,
            'currentPage': currentPage,
            'pageSize': pageSize,
            'resultRows': resultRows,
        }
        return context
            
            
        
    def advanced_query(self, q, num_pages, start_page):
        
        url = self.baseurl
        
        dateFormat = "%Y-%m-%dT%H:%M:%S.%fZ"        
            
        params = {
            'query': q,
            'count': num_pages,
            'start': start_page,
            'apiKey': self.apiKey,
        }
        
        response = requests.request("GET", url, params=params)
        data = response.json()
        
        # Populate variables, proof of concept, this needs significant rework to be fully viable.
        totalResults = data['search-results']['opensearch:totalResults']
        currentPage = data['search-results']['opensearch:startIndex']
        pageSize = data['search-results']['opensearch:itemsPerPage']
        entries = data['search-results']['entry']
        
        
        resultRows = []
        
        if int(totalResults) != 0:
            for entry in entries:
            
                loadDateTime = datetime.strptime(entry['load-date'], dateFormat)
            
                row = {
                    "identifier": entry['dc:identifier'],
                    "url": entry['prism:url'],
                    "title": entry['dc:title'],
                    "creator": entry['dc:creator'],
                    "publication": entry['prism:publicationName'],
                    "loadDate": loadDateTime.strftime('%y-%m-%d'),
                } 
            
                resultRows.append(row)
            
            
            
        context = {
            'results': totalResults,
            'currentPage': currentPage,
            'pageSize': pageSize,
            'resultRows': resultRows,
        }
        return context
        
        
        