import unittest

from new.newsapi import cli

class test_is_newsapi_article(unittest.TestCase):
    def test_is_newsapi(self):
        self.assertEqual(is_newsapi(" "))
    
    def test_request_response(self):
        response = 200
        self.assertEqual(response.status_code,200)
        pass
    
    def test_page_Size(self):
        pageSize = 10
        self.assertEqual(pageSize(),10)
        pass




if __name__ == '__main__':
        unittest.main()






