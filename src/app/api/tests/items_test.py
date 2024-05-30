import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import cookies
from src.app.api.items import search
import unittest

#auth = cookies.load_auth_cookie()

#c = {
 #   auth[0]: auth[1]
#}

class TestSearch(unittest.TestCase):
    def test_failure(self):        
        with self.assertRaises(Exception):
            search()
    
            
if __name__ == "__main__":
    unittest.main()