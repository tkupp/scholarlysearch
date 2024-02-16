from django.test import TestCase

from .elsevier_rest_class import Elsevier_rest
from .arxiv_rest_class import Arxiv_rest

class elsevierRestTestCase(TestCase):
    
    def setUp(self):
        # Every test needs access to the Elseviser_rest class.
        self.factory = Elsevier_rest()
        
    def test_basicQuery(self): 
        
        q = 'AI generative'
        context = self.factory.basicQuery(q) 
        

        print('Number of results from Elsevier basicQuery: ' + context['results'])

        
class arxivRestTestCase(TestCase):
    
    def setUp(self):
        # Every test needs access to the Arxiv_rest class.
        self.factory = Arxiv_rest()
        
    def test_basicQuery(self): 
        # Test that query is passed through and returns expected results.
        q = 'AI generative'
        context = self.factory.basicQuery(q) 
        
        print('Number of results from arXiv basicQuery: ' + context['results'])

        for entry in context['resultRows']:
            print(entry['author'])
            print(entry['title'])

    # def test_startDate(self):
    #     # Test that start date filter is applied and no earlier results are returned.
    #     q = 'AI generative'
    #     # start = "-%m-%dT%H:%M:%SZ"
    #     context = self.factory.basicQuery(q) 
        
    #     print('Number of results from arXiv basicQuery: ' + context['results'])

    #     for entry in context['resultRows']:
    #         print(entry['published'])

    # def test_endDate(self):
    #     # Test that end date filter is applied and no later results are returned.
    #     q = 'AI generative'
    #     # end = "-%m-%dT%H:%M:%SZ"
    #     context = self.factory.basicQuery(q) 
        
    #     print('Number of results from arXiv basicQuery: ' + context['results'])

    #     for entry in context['resultRows']:
    #         print(entry['published'])

