from flask_restful import fields
from project import db

user_fields = {
    'id': fields.String,
    'username': fields.String,
    'password': fields.String,
    'role': fields.String
}

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    
