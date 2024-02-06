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
        
        dateFormat = "%Y-%m-%dT%H:%M:%SZ"    
            
        params = {
            'search_query': q,
        }

        response = requests.request("GET", url, params=params)

        # Convert xml API output to dict
        data = xmltodict.parse(response.content)

        # These will need to be reworked for the arxiv output.

        totalResults = data['feed']['opensearch:totalResults']['#text']
        currentPage = data['feed']['opensearch:startIndex']['#text']
        pageSize = data['feed']['opensearch:itemsPerPage']['#text']
        entries = data['feed']['entry']
        
        resultRows = []
        
        if int(totalResults) != 0:
            for entry in entries:
            
                publishedDateTime = datetime.strptime(entry['published'], dateFormat)
            
                row = {
                    "id": entry['id'],
                    "title": entry['title'],
                    "author": entry['author'],
                    "published": publishedDateTime.strftime('%y-%m-%d'),
                } 
            
                resultRows.append(row)
            
            
            
        context = {
            'results': totalResults,
            'currentPage': currentPage,
            'pageSize': pageSize,
            'resultRows': resultRows,
        }
        return context
            
            
        
        
        
        
            
        