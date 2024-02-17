from django.test import TestCase
from django.test import Client

class Test_views(TestCase):
    
    def setUp(self):
        
        self.client = Client()
    
    def test_search_main(self):
            
        response = self.client.get("/search/")
            
        print("status code: " + str(response.status_code))
        self.assertTrue(response.status_code == 200)