from flask import Flask, render_template, request
from src.classes.Api import getCultureById, filterCities, isBestPeriod
from src.classes.controllers.ComercialDataController import getCulturesAlphaOrdered

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("choose_culture.html", cultures=getCulturesAlphaOrdered(), errors={})

@app.route("/send-search", methods=["POST"])
def sendSearch():
    if request.method == "POST":
        cultureId = request.form.get("cultureId")
        period = request.form.get("period")
        filterType = request.form.get("type")
        
        if(period and filterType):
            return render_template("result.html", culture=getCultureById(cultureId), cities=filterCities(cultureId, str(period), str(filterType)), period=period, filterType=filterType, isBestPeriod=isBestPeriod(cultureId, period))
        
        errors = {
            "message": "Houve erro ao ler o campos do formulário!"
        }

        return render_template("choose_culture.html", errors=errors)