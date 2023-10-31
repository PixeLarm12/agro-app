from flask import Flask, render_template, request
from src.classes.Controller import getCulturesFromApi, getCultivationByCultureId

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html", cultures=getCulturesFromApi(), errors={})

@app.route("/send-search", methods=["POST"])
def sendSearch():
    if request.method == "POST":
        cultureId = request.form.get("cultureId")
        
        if(cultureId):
            return render_template("cultivation.html", culture=getCultivationByCultureId(cultureId), cities=CidadesPorCultura(cultureId))
        
        errors = {
            "message": "Houve erro ao ler o campos do formulário!"
        }

        return render_template("search.html", errors=errors)