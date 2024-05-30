from src.app.utils import config_functions, cookies
import requests
from requests import Response
import json

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}

endpoints = config_functions.read_json("src/app/config/endpoints.json")
BASE_URL = endpoints["BASE_URL"]
endpoints = endpoints["endpoints"]

def build_url(base_url: str, endpoint: str, params: list = [], **kwargs) -> str:
    url = f"{base_url}{endpoint}?"
    for param in params:
        if param in kwargs:
            url += f"{param}={kwargs[param]}&"
    return url.rstrip('&')

def check_cookies(cookies:list=[]):
    if len(cookies) == 0 or cookies == None:
        raise Exception("Error: cookies were not given. ❌")

def search(cookies:list=[], **kwargs):
    check_cookies(cookies=cookies)
            
    endpoint: str = endpoints["search"]["value"]
    params: list = endpoints["search"]["params"]
    
    url: str = build_url(base_url=BASE_URL, endpoint=endpoint, params=params, **kwargs)
        
    try:
        res: Response = requests.get(url=url, headers=headers, cookies=cookies)
        res.raise_for_status()

        data = res.json()
        
        return data
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
        
def similar_items(cookies, item_id: str):
    endpoint: str = endpoints["similar_items"]["value"].replace("{id}", item_id)
    url: str = f"{BASE_URL}{endpoint}"
        
    try:
        res: Response = requests.get(url=url, headers=headers, cookies=cookies)
        res.raise_for_status()

        data = res.json()
        
        return data
    except requests.RequestException as e:
        raise Exception(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}")
