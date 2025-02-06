from flask import Flask, render_template, request

from .silpo_api import Product

app = Flask(__name__)


@app.route("/")
def index():
    search_query = request.args.get("q")
    if search_query:
        print("Searching " + search_query)
        products = Product.search(search_query)
        return render_template("index.html", products=products, count=len(products), search_query=search_query)
    return render_template("index.html")
