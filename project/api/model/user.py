from flask_restful import fields
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from project import db, Base


user_fields = {
    'id': fields.String,
    'username': fields.String,
    'password': fields.String,
    'create_date': fields.String,
    'update_date': fields.String,
    'del_date': fields.String,
    'role': fields.String
}

class User(Base, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    role = Column(String(80), nullable=False)
    create_date = Column(String(120), nullable=False)
    update_date = Column(String(120))
    del_date = Column(String(120))
    
    goals = relationship("Goal", back_populates="user")
    # cash_flow_statements = relationship("CashFlowStatement", back_populates="user")
    
