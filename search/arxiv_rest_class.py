import xmltodict
import requests
from more_itertools import collapse
from datetime import datetime


class Arxiv_rest():
    
    def __init__(self, *args, **kwargs):
        
        self.baseurl = "http://export.arxiv.org/api/query"
        

    def multiAuthor(self, authors):

        # Method for getting multiple authors collapsed into a single list
        author_list = [d['name'] for d in collapse(authors, base_type=dict)]

        return author_list
   
   
    def basicQuery(self, q):
        
        url = self.baseurl
        
        dateFormat = "%Y-%m-%dT%H:%M:%SZ"    
            
        params = {
            'search_query': q,
        }

        response = requests.request("GET", url, params=params)

        # Convert xml API output to dict
        data = xmltodict.parse(response.content)

        # Parse results data from dict
        totalResults = data['feed']['opensearch:totalResults']['#text']
        currentPage = data['feed']['opensearch:startIndex']['#text']
        pageSize = data['feed']['opensearch:itemsPerPage']['#text']
        entries = data['feed']['entry']
        
        resultRows = []
        
        if int(totalResults) != 0:
            
            for entry in entries:
            
                publishedDateTime = datetime.strptime(entry['published'], dateFormat)
            
                author_entry = self.multiAuthor(entry['author'])

                row = {
                    "id": entry['id'],
                    "title": entry['title'],
                    "author": author_entry,
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
            
            
        
        
        
        
            
        