from . import constant
from ..model.goal import Goal as GoalModel

def validate_input_post_goal(data):

    if int(data[constant.goal_target]) <= 0:
        raise Exception('target must not lower than 0')
    else:
        return GoalModel(
                data[constant.goal_name], 
                data[constant.goal_target], 
                data[constant.goal_start_date], 
                data[constant.goal_end_date])