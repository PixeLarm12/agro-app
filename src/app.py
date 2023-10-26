from flask import Flask, render_template
from src.classes.cultivation import getTypesOfCulture

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html", cultures=getTypesOfCulture())