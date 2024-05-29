from flask import Flask
from Vinted import Vinted

app = Flask(__name__)

v = Vinted()

@app.route("/")
def search_items():
    return v.search_items(page=1, search_text="Jordan")

if __name__ == "__main__":
    app.run(debug=True)