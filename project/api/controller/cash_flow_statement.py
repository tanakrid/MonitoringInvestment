from ..util import constant
from project.api.model.cash_flow_statement import CashFlowStatement
from project.api.model.user import User
import traceback 

def create_cash_flow_statement(args):

    return CashFlowStatement(
        create_date=args[constant.cash_flow_statement_create_date],
        user_id = args['user_id'],
        user = User.query.filter_by(id=args['user_id']).first()
    )