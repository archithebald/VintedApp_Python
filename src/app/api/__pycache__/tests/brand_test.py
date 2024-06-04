import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.api.brand import filter_brand
import unittest

class TestFilterBrand(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.id_response = filter_brand(brand_id=6451)
        self.name_response = filter_brand(name="internet")
        self.luxury_response = filter_brand(is_luxury=True)
        self.authenticity_response = filter_brand(authenticity_check_required=True)
        
    def test_failure(self):   
        with self.assertRaises(Exception):
            filter_brand()
            
    def test_name_param_response_success(self):
        self.assertIsInstance(self.name_response, list)   
        
    def test_luxury_param_response_success(self):
        self.assertIsInstance(self.luxury_response, list)  
        
    def test_authenticity_param_response_success(self):
        self.assertIsInstance(self.authenticity_response, list)  
        
    def test_id_param_response_success(self):
        self.assertIsInstance(self.id_response, list)                                   
        
if __name__ == "__main__":
    unittest.main()