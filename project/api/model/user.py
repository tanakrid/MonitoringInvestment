from flask_restful import fields
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from project import db


user_fields = {
    'id': fields.String,
    'username': fields.String,
    'password': fields.String,
    'create_date': fields.String,
    'update_date': fields.String,
    'del_date': fields.String,
    'role': fields.String
}
Base = declarative_base()
class User(Base, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    role = Column(String(80), nullable=False)
    create_date = Column(String(120), nullable=False)
    update_date = Column(String(120))
    del_date = Column(String(120))
    
    cash_flow_statement = relationship("CashFlowStatement", back_populates="User")
    goal = relationship("Goal", back_populates="User")
    
