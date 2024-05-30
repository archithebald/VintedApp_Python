import sys
import os
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
import unittest
from src.app.utils.tests import import_tests
  
if __name__ == "__main__":
    tests_dir = os.path.join(os.path.dirname(__file__))
    import_tests(tests_dir)
    
    unittest.main()