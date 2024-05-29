from utils import config_functions, cookies
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}

endpoints = config_functions.read_json("src/app/config/endpoints.json")
BASE_URL = endpoints["BASE_URL"]
endpoints = endpoints["endpoints"]

def search(cookies, **kwargs):
    endpoint = endpoints["search"]["value"]
    params = endpoints["search"]["params"]
    
    url = BASE_URL + endpoint + "?"
    
    for param in params:
        arg = None
        
        if param in kwargs["kwargs"]:
            arg = kwargs["kwargs"][param]
        
        if arg:
            url += f"{param}={arg}&"
    
    print("Url: ", url)
    res = requests.get(url=url, headers=headers, cookies=cookies)
    
    try:
        data = res.json()
        
        return data
    except Exception as e:
        print(f"Error: {e}")