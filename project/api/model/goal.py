from flask_restful import fields
from project import db

goal_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'target': fields.Integer,
    'start_date': fields.String,
    'end_date': fields.String,
    'progress': fields.Float
}

class Goal(db.Model):
    
    # def __init__(self, name, target, start_date = None, end_date = None):
    #     self.id = ""
    #     self.name = name
    #     self.target = target
    #     self.start_date = start_date
    #     self.end_date = end_date
    #     self.progress = 0

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    target = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.String(120), nullable=False)
    end_date = db.Column(db.String(120), nullable=False)
    progress = db.Column(db.Float, nullable=False)
    
