# Vinted App in Python

## Description

This is a Vinted Api Wrapper which you can use in python for various projects in which you need to include some vinted features (e.g : Searching items based on query).

## Installation

1. Install package : `pip install pythed`

## Example

```
from pythed.app.Vinted import Vinted

app = Vinted()

brands = app.get_brands(brand_names=["Jordan", "Nike"])
brand1 = brands[0]["id"]
brand2 = brands[1]["id"]

items = app.search_items(search_text="Jordan", perPage=1, brand_ids=[brand1, brand2], price_to=15)

print(items)
```

## Emoji Code for commits

- 🔄 Updated README file.
- 🛠️ Created new feature.
- 🐛 Fixed a bug.
- ✅ Added tests.
- 🔒️ Fixed security issues.
- 🔖 New release.
- 🚧 Work in progress.
- ⬆️ Updgraded dependencies.
- ⬇️ Downgraded dependencies.
- ♻️ Refactored code.
- ➕ Added a dependency.
- ➖ Removedg a dependency.
- 🔧 Changed configuration files.
- 🙈 Updating .gitignore file.

## Contact

Discord: archibald1789
