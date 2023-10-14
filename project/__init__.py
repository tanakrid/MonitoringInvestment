from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base


db = SQLAlchemy()
migrate = None
Base = None

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)

    migrate = Migrate(app, db)

    Base = declarative_base()

    setResource(Api(app))

    # @app.route("/home")
    # def home():
    #     return render_template("home.html")

    # @app.route("/about")
    # def about():
    #     return render_template("about.html")

    return app

def setResource(api_resource):
    from project.api.resource.goal_list import GoalList, Goal
    api_resource.add_resource(GoalList, '/goal')
    api_resource.add_resource(Goal, '/goal/<id>')

import config
from . import api