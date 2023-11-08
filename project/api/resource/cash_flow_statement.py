from project.api.model.cash_flow_statement import CashFlowStatement as CashFlowStatementModel, cash_flow_statement_fields
from project import db
from project.api.controller import cash_flow_statement as CashFlowStatementController

from flask_restful import Resource, marshal_with, reqparse
from flask import abort
import traceback 

parser = reqparse.RequestParser()
parser.add_argument('create_date', type=str, required=True)
parser.add_argument('user_id', type=str, required=True)

class CashFlowStatementlList(Resource):

    @marshal_with(cash_flow_statement_fields)
    def get(self):
        return CashFlowStatementModel.query.all()
    
    @marshal_with(cash_flow_statement_fields)
    def post(self):
        args = parser.parse_args()
        cash_flow_statement = None
        try:
            cash_flow_statement = CashFlowStatementController.create_cash_flow_statement(args)
        except Exception:
            traceback.print_exc() 
            return abort(403, "Invalid input parameter")
        db.session.add(cash_flow_statement)
        db.session.commit()
        return cash_flow_statement
    
class CashFlowStatement(Resource):

    @marshal_with(cash_flow_statement_fields)
    def get(self, id):
        cash_flow_statement = CashFlowStatementModel.query.filter_by(id=id).first()
        if not cash_flow_statement:
            return abort(404)
        return cash_flow_statement
    
    @marshal_with(cash_flow_statement_fields)
    def patch(self, id):
        args = parser.parse_args()
        cash_flow_statement = CashFlowStatementModel.query.filter_by(id=id).first()
        if not cash_flow_statement:
            return abort(404, 'Cash flow statement not found!')
        try:
            tmp = CashFlowStatementController.create_cash_flow_statement(args)

            # bind data from args to existing data
            cash_flow_statement.id = id
            cash_flow_statement.create_date = tmp.create_date
            cash_flow_statement.update_date = tmp.update_date
            cash_flow_statement.del_date = tmp.del_date
            cash_flow_statement.user_id = tmp.user_id

            db.session.commit()
        except Exception:
            return abort(403, "Invalid input parameter")
        return cash_flow_statement
    
    @marshal_with(cash_flow_statement_fields)
    def delete(self, id):
        cash_flow_statement = CashFlowStatementModel.query.filter_by(id=id).first()
        if not cash_flow_statement:
            return abort(404, 'Cash flow statement not found!')
        db.session.delete(cash_flow_statement)
        db.session.commit()