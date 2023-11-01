from flask import Flask, render_template, request
from src.classes.Database import getCultureById, citiesByCulture, Cultures

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html", cultures=Cultures(), errors={})

@app.route("/send-search", methods=["POST"])
def sendSearch():
    if request.method == "POST":
        cultureId = request.form.get("cultureId")
        
        if(cultureId):
            return render_template("cultivation.html", culture=getCultureById(cultureId), cities=citiesByCulture(cultureId))
        
        errors = {
            "message": "Houve erro ao ler o campos do formulário!"
        }

        return render_template("search.html", errors=errors)