from . import constant
from project.api.model.goal import Goal as GoalModel

def validate_input_post_goal(args):

    if int(args[constant.goal_target]) <= 0:
        raise Exception('target must not lower than 0')
    else:
        return GoalModel(
            name=args[constant.goal_name], 
            target=args[constant.goal_target], 
            start_date=args[constant.goal_start_date], 
            end_date=args[constant.goal_end_date],
            progress= 0
        )