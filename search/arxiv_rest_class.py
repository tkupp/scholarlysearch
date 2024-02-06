import os
import xmltodict
import pprint
import simplejson
import json
import requests
from datetime import datetime


class Arxiv_rest():
    
    def __init__(self, *args, **kwargs):
        
        self.baseurl = "http://export.arxiv.org/api/query"
        
        
    def basicQuery(self, q):
        
        url = self.baseurl
        
        dateFormat = "%Y-%m-%dT%H:%M:%S.%fZ"    
            
        params = {
            'search_query': q,
        }

        response = requests.request("GET", url, params=params)

        # Convert xml API output to json
        data = json.dumps(xmltodict.parse(response.content))
        
        # These will need to be reworked for the arxiv output.

        # totalResults = data['search-results']['opensearch:totalResults']
        # currentPage = data['search-results']['opensearch:startIndex']
        # pageSize = data['search-results']['opensearch:itemsPerPage']
        # entries = data['search-results']['entry']
        
        
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
            
            
        
        
        
        
            
        