from flask_restful import fields
from project import db, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

cash_flow_statement_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer, 
    'create_date': fields.String,
    'update_date': fields.String,
    'del_date': fields.String
}

class CashFlowStatement(Base, db.Model):
    __tablename__ = 'cash_flow_statements'

    id = Column(Integer, primary_key=True)
    create_date = Column(String(120), nullable=False)
    update_date = Column(String(120))
    del_date = Column(String(120))

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="cash_flow_statements")
    # transactions = relationship("Transaction", back_populates="cash_flow_statement")
    
