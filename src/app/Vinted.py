import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import cookies
from src.app.api.items import search, similar_items
from src.app.api.brand import get_brands, filter_brand 
from src.app.api.users import get_user_info

class Vinted():
    def __init__(self):
        self.auth_cookie = cookies.load_auth_cookie() # [0] - Cookie name ||| [1] - Cookie value
        self.cookies = {self.auth_cookie[0]: self.auth_cookie[1]}
        
    def search_items(self, **kwargs) -> list:
        data = search(self.cookies, kwargs=kwargs)
        
        return data["items"]
    
    def similar_items(self, item_id: str) -> list:
        data = similar_items(self.cookies, item_id=item_id)
        
        return data["items"]
    
    def get_all_brands(self) -> list:
        return get_brands()
    
    def get_brand(self, brand_id:int=None, brand_name:str=None, is_luxury:bool=None, requires_authenticity_check:bool=None) -> list:
        return filter_brand(brand_id, brand_name, is_luxury, requires_authenticity_check)
    
    def get_user_info(self, user_id:str):
        return get_user_info(self.cookies, user_id=user_id)