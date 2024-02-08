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
        
        q = 'AI generative'
        context = self.factory.basicQuery(q) 
        
        print('Number of results from arXiv basicQuery: ' + context['results'])

        for entry in context['resultRows']:
            print(entry['author'])

