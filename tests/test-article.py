import unittest

class Articles:
    '''
    News Articles class to define news articles objects
    '''
    def __init__(self,title,urlToImage,content,author,publishedAt,url):
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.author = author
        self.publishedAt= publishedAt
        self.url=url

class TestArticles(unittest.TestCase):
    '''
    Test class that defines test cases for the articles class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_article = Articles("","","","","","") # create an articles object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_article.title,"")
        self.assertEqual(self.new_article.urlToImage,"")
        self.assertEqual(self.new_article.content,"")
        self.assertEqual(self.new_article.author,"")
        self.assertEqual(self.new_article.publishedAt,"")
        self.assertEqual(self.new_article.url,"")


if __name__ == '__main__':
    unittest.main()