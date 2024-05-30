import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import cookies
from src.app.api.items import search, similar_items
import unittest
from unittest.mock import patch
from requests import RequestException

## TODO - create test class for similar items and create success function for both tests

auth = cookies.load_auth_cookie()

c = {
   auth[0]: auth[1]
}    

class TestSearch(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.response = similar_items(cookies=c, item_id="4574942465")  

    
    def test_failure(self):        
        with self.assertRaises(Exception):
            search()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)                  
    
class TestSimilarItems(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.response = similar_items(cookies=c, item_id="4574942465")  

    def test_failure(self):
        with self.assertRaises(Exception):
            similar_items()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)                  
    
if __name__ == "__main__":
    unittest.main()