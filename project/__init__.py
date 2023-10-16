from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = None
Base = None

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)

    setResource(Api(app))

    return app

def setResource(api_resource):
    from project.api.resource.goal_list import GoalList, Goal
    api_resource.add_resource(GoalList, '/goal')
    api_resource.add_resource(Goal, '/goal/<id>')

import config
from . import api