from flask.views import MethodView

class HomeController(MethodView):
    def get(self):
        return "Welcome to Main Page!"