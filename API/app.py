from flask import Flask

from controller.RecommendationsController import RecommendationsController

app = Flask(__name__)

class App:
    def __init__(self, app):
        RecommendationsController.register_routes(app)

if __name__ == '__main__':
    app_instance = App(app)
    app.run(debug=True)
