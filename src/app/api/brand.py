import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import config_functions

## TODO : Catch errors in the filterbrand

brands_data: dict = config_functions.read_json("src/app/config/brands.json")

def filter_brand(brand_id:int = None, slug:str = None, is_luxury:bool = None, authenticity:bool = False):
    filtered = []
    
    for brand in brands_data:
        if brand_id and brand["id"] == brand_id:
            filtered.append(brand)
        if slug and slug in brand["name"]:
            filtered.append(brand)
        if is_luxury and brand["is_luxury"] == is_luxury:
            filtered.append(brand)
        if authenticity and brand["requires_authenticity_check"] == authenticity:
            filtered.append(brand)
        
    return filtered