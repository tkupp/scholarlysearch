from django.test import TestCase

from .elsevier_rest_class import Elsevier_rest

class Elsevier_rest_tests(TestCase):
    
    def setUp(self):
        # Every test needs access to the Elseviser_rest class.
        self.factory = Elsevier_rest()
        
    def test_basic_query(self): 
        
        q = 'AI generative'
        context = self.factory.basic_query(q) 
        
        number_results = int(context['results'])
        
        # This query should always return results.
        self.assertTrue(number_results > 0)
        