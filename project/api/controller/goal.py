from ..util import constant
from project.api.model.goal import Goal as GoalModel
from project.api.model.user import User
import traceback 

def validate_input_post_goal(args):

    if int(args[constant.goal_target]) <= 0:
        raise Exception('target must not lower than 0')
    else:
        return GoalModel(
            name=args[constant.goal_name], 
            target=args[constant.goal_target], 
            start_date=args[constant.goal_start_date], 
            end_date=args[constant.goal_end_date],
            progress= 0,
            create_date=args[constant.goal_start_date],
            user_id = args['user_id'],
            user = User.query.filter_by(id=args['user_id']).first()
        )