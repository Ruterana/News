import unittest
from app.models import Sources

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(id,name,author,title,description,url,urlToImage,publicedAt)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))