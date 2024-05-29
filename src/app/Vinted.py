from utils import config_functions, cookies
from api import search

class Vinted:
    def __init__(self):
        self.auth_cookie = cookies.load_auth_cookie() # [0] - Cookie name ||| [1] - Cookie value
        self.cookies = {self.auth_cookie[0]: self.auth_cookie[1]}
        
    def search_items(self, **kwargs):
        data = search(self.cookies, kwargs=kwargs)
        
        return data["items"]