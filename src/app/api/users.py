import requests
from requests import Response
import json
from src.app.api import *

def get_user_info(cookies:list=[], **kwargs):
    check_cookies(cookies=cookies)
    
    endpoint: str = endpoints["search"]["value"]
    params: list = endpoints["search"]["params"]