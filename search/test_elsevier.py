from django.test import TestCase

from .elsevier_rest_class import Elsevier_rest

class Elsevier_rest_tests(TestCase):
    
    def setUp(self):
        # Every test needs access to the Elseviser_rest class.
        self.factory = Elsevier_rest()
            
    def test_query(self):
        
        q = 'AI generative'
        num_pages = 100
        start_page = 2
        
        context = self.factory.query(q, num_pages, start_page) 
        
        number_results = int(context['results'])
        
        # This query should always return results.
        self.assertTrue(number_results > 0)    
        
