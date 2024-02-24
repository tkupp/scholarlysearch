from django.test import TestCase

from .elsevier_rest_class import Elsevier_rest

class Elsevier_rest_tests(TestCase):
    
    def setUp(self):
        # Every test needs access to the Elseviser_rest class.
        self.factory = Elsevier_rest()
    
    '''
    Test that calling the remote API returns a 200 status.  If it does not, then there is 
    either something wrong with the scholarlysearch code, or the upstream system has an issue.
    As this application is all about access to upstream systems, it is important to know if it is reachable. 
    '''        
    def test_query(self):
        
        q = 'AI generative'
        num_pages = 10
        start_page = 2
        
        context = self.factory.query(q, num_pages, start_page) 
        
        status = int(context['status'])
        
        # This query should always return results.
        self.assertTrue(status == 200)    
        
    '''
    While the test_query function is a broad test that tests for connectivity, this test is to 
    insure that the issue is not an upstream authorization error.  If this test fails, then 
    the test_query will also fail. If this test succeeds and the test_query fails, then we know we have 
    an authorization error.
    '''    
    def test_elseviver_authorization(self):
        
        q = 'AI generative'
        num_pages = 10
        start_page = 2
        
        context = self.factory.query(q, num_pages, start_page) 
        
        status = int(context['status'])
        
        # This query should always return results.
        self.assertFalse(status == 401)    
