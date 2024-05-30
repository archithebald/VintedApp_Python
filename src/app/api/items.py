from src.app.utils import config_functions, cookies
import requests
from requests import Response

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}

endpoints = config_functions.read_json("src/app/config/endpoints.json")
BASE_URL = endpoints["BASE_URL"]
endpoints = endpoints["endpoints"]

def search(cookies=[], **kwargs):
    if len(cookies) == 0 or cookies == None:
        raise Exception("Error: cookies were not given. ❌")
            
    endpoint: str = endpoints["search"]["value"]
    params: list = endpoints["search"]["params"]
    
    url: str = BASE_URL + endpoint + "?"
    
    for param in params:
        arg = None
        
        if param in kwargs:
            arg = kwargs[param]
        
        if arg:
            url += f"{param}={arg}&"
        
    try:
        res = requests.get(url=url, headers=headers, cookies=cookies)

        data = res.json()
        
        return data
    except Exception as e:
        raise Exception(e)
        
def similar_items(cookies, item_id: str):
    endpoint: str = endpoints["similar_items"]["value"]
    endpoint: str = endpoint.replace("{id}", item_id)
    
    url: str = BASE_URL + endpoint
    
    res: Response = requests.get(url=url, headers=headers, cookies=cookies)
    
    try:
        data = res.json()
        
        return data
    except Exception as e:
        print(f"Error: {e}")