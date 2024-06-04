import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import cookies
from src.app.api.users import get_user_info, get_user_reviews
import unittest

auth = cookies.load_auth_cookie()

c = {
   auth[0]: auth[1]
}    

class TestGetUserInfo(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.response = get_user_info(cookies=c, user_id="155748220")

    def test_failure(self):   
        with self.assertRaises(Exception):
            get_user_info()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)                                 
     
class TestGetUserReviews(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.response = get_user_reviews(cookies=c, user_id="155748220")

    def test_failure(self):   
        with self.assertRaises(Exception):
            get_user_reviews()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)   
        
if __name__ == "__main__":
    unittest.main()