from . import api

from flask import Flask, render_template
from flask_restful import Api

from project.api.resource.goal_list import GoalList, Goal

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # @app.route("/home")
    # def home():
    #     return render_template("home.html")

    # @app.route("/about")
    # def about():
    #     return render_template("about.html")

    api.add_resource(GoalList, '/goal')
    api.add_resource(Goal, '/goal/<id>')

    return app