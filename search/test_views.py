from django.test import TestCase
from django.test import Client

class Test_views(TestCase):
    
    def setUp(self):
        
        self.client = Client()
    
    def test_search_main(self):
            
        response = self.client.get("/search/")
            
        self.assertTrue(response.status_code == 200)
        
    def test_search_elsevier(self):
        
        response = self.client.get("/search/searchElsevier")   
        
        self.assertTrue(response.status_code == 200)