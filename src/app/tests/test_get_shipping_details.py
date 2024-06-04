import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app import Vinted

app = Vinted.Vinted()

print(app.get_shipping_details(item_id="4596708317"))