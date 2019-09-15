import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(id,name,description,url,category,language,country)

    def test_instant(self):
        self.assertTrue(isinstant(self.new_sources,Sources))