import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import cookies
from src.app.api.items import search, similar_items

class Vinted():
    def __init__(self):
        self.auth_cookie = cookies.load_auth_cookie() # [0] - Cookie name ||| [1] - Cookie value
        self.cookies = {self.auth_cookie[0]: self.auth_cookie[1]}
        
    def search_items(self, **kwargs) -> dict:
        data = search(self.cookies, kwargs=kwargs)
        
        return data["items"]
    
    def similar_items(self, item_id: str) -> dict:
        data = similar_items(self.cookies, item_id=item_id)
        
        return data["items"]