from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

app.add_url_rule(routes["home-page"],view_func=routes["home-controller"])