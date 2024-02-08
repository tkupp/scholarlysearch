from django.test import TestCase

from .elsevier_rest_class import Elsevier_rest

class elsevierRestTestCase(TestCase):
    
    def setUp(self):
        # Every test needs access to the Elseviser_rest class.
        self.factory = Elsevier_rest()
        
    def test_basicQuery(self): 
        
        q = 'AI generative'
        context = self.factory.basicQuery(q) 
        
        print('')
        print('Number of results from basicQuery: ' + context['results'])
        print('')
        

