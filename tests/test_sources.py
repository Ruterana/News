import unittest
from app.models import sources

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',"https://abcnews.go.com',general)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))