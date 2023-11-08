from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from sqlalchemy.orm import declarative_base

db = SQLAlchemy()
jwt = JWTManager()
migrate = None
Base = declarative_base()

def create_app(parameter):
    app = Flask(__name__)
    app.config.update(parameter)

    db.init_app(app)
    jwt.init_app(app)

    setResource(Api(app))

    return app

def setResource(api_resource):
    from project.api.resource.goal_list import GoalList, Goal
    api_resource.add_resource(GoalList, '/goal')
    api_resource.add_resource(Goal, '/goal/<id>')

    from project.api.resource.login import Register, Login, ProtectedResource, Logout
    api_resource.add_resource(Register, '/register')
    api_resource.add_resource(Login, '/login')
    api_resource.add_resource(ProtectedResource, '/protected_resource')
    api_resource.add_resource(Logout, '/logout')

    from project.api.resource.cash_flow_statement import CashFlowStatementlList, CashFlowStatement
    api_resource.add_resource(CashFlowStatementlList, '/cash_flow_statement')
    api_resource.add_resource(CashFlowStatement, '/cash_flow_statement/<id>')

from . import api