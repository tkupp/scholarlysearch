from django.test import TestCase
from django.test import Client

'''
Test functions for the 'search' application UI views.
'''
class Test_views(TestCase):
    
    '''
    Every test needs a client. Set it up when the class is instantiated.
    '''
    def setUp(self):
        
        self.client = Client()
    
    '''
    Test that the main page loads correctly. Should return a 200 status code.
    '''
    def test_search_main(self):
            
        response = self.client.get("/search/")
            
        self.assertTrue(response.status_code == 200)
        
    '''
    Test that the "elsevier' search page loads correctly. Should return a 200 status code.
    '''    
    def test_search_elsevier(self):
        
        response = self.client.get("/search/searchElsevier")   
        
        self.assertTrue(response.status_code == 200)