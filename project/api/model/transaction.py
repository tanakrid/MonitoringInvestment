from flask_restful import fields
from project import db
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

goal_fields = {
    'id': fields.Integer,
    'tran_type': fields.String,
    'desc': fields.String,
    'amount': fields.Float,
    'catagory_type': fields.String,
    'custom_catagory_type': fields.String,
    'create_date': fields.String,
    'update_date': fields.String,
    'del_date': fields.String,
    'cash_flow_id': fields.Integer,
}
Base = declarative_base()
class Transaction(Base, db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    tran_type = Column(String(80), nullable=False)
    desc = Column(String(120), nullable=True)
    amount = Column(Float, nullable=False)
    catagory_type = Column(String(120), nullable=False)
    custom_catagory_type = Column(String(120), nullable=True)
    create_date = Column(String(120), nullable=False)
    update_date = Column(String(120))
    del_date = Column(String(120))
    
    cash_flow_id = Column(Integer, ForeignKey('cash_flow_statements.id'))
    cash_flow_statement = relationship("CashFlowStatement", back_populates="Transactions")
