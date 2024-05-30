import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)