from django.test import TestCase

from .arxiv_rest_class import Arxiv_rest
        
class arxiv_rest_tests(TestCase):
    
    def setUp(self):
        # Every test needs access to the Arxiv_rest class.
        self.factory = Arxiv_rest()
        
    def test_basic_query(self): 

        q = 'AI generative'
        context = self.factory.basicQuery(q)
                
        number_results = int(context['results'])

        # This query should always return results.
        self.assertTrue(number_results > 0)

    def test_single_author(self):

        example_author = [{'name' : 'Bin Liu'}]
        author_test = self.factory.multiAuthor(example_author)
                
        number_authors = len(author_test)

        # This should only return one result.
        self.assertTrue(number_authors == 1)

    def test_multiple_authors(self):

        example_authors = [{'name' : 'Aastha Pant'}, {'name' : 'Rashina Hoda'}, {'name' : 'Simone V. Spiegler'}, {'name' : 'Chakkrit Tantithamthavorn'}]

        author_test = self.factory.multiAuthor(example_authors)
                
        number_authors = len(author_test)
        
        # print('Author list: ' + ', '.join(author_test))
        
        # This should return exactly four results.
        self.assertTrue(number_authors == 4)
        


