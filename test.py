from pythed.app import Vinted

app = Vinted.Vinted()

items = app.search_items(search_text="Jordan")

print(items)