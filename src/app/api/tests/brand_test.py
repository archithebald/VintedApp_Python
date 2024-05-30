import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.api.brand import filter_brand
import unittest

class TestFilterBrand(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.response = filter_brand()

    def test_failure(self):   
        with self.assertRaises(Exception):
            search()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)                                    