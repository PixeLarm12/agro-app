from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    cities = [
        {"id": 1, "name": "Bauru"},
        {"id": 22, "name": "Araraquara"},
        {"id": 12, "name": "Jau"},
    ]

    return render_template("search.html", cities=cities)