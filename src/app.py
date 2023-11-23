from flask import Flask, render_template, request
from src.classes.Database import getCultureById, filterCities, Cultures

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("choose_culture.html", cultures=Cultures(), errors={})

@app.route("/send-search", methods=["POST"])
def sendSearch():
    if request.method == "POST":
        cultureId = request.form.get("cultureId")
        period = request.form.get("period")
        
        if(period):
            return render_template("result.html", culture=getCultureById(cultureId), cities=filterCities(cultureId, period), period=period)
        
        errors = {
            "message": "Houve erro ao ler o campos do formulário!"
        }

        return render_template("search.html", errors=errors)