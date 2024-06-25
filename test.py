from pythed.app import Vinted

app = Vinted.Vinted()

brand1 = app.get_brand(brand_name="Jordan")[0]["id"]
brand2 = app.get_brand(brand_name="Nike")[0]["id"]

items = app.search_items(search_text="Jordan", perPage=1, brand_ids=[brand1, brand2])

print(items)