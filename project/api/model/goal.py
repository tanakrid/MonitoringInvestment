from flask_restful import fields
from project import db
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

goal_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'target': fields.Integer,
    'start_date': fields.String,
    'end_date': fields.String,
    'progress': fields.Float
}
Base = declarative_base()
class Goal(Base, db.Model):
    __tablename__ = 'goal'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    target = Column(Integer, nullable=False)
    start_date = Column(String(120), nullable=False)
    end_date = Column(String(120), nullable=False)
    progress = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="goals")
    
