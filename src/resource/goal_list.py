from ..model.goal import Goal as GoalModel, goal_fields
from ..util import constant

import json
from flask_restful import Resource, marshal_with, fields
from flask import jsonify, request, abort

goal_list = {}
goal_list_fields = {}
count = 0

class GoalList(Resource):

    @marshal_with(goal_list_fields)
    def get(self):
        return goal_list
    
    def post(self):
        global count
        data = json.loads(request.data)
        tmp = GoalModel(
            data[constant.goal_name], 
            data[constant.goal_target], 
            data[constant.goal_start_date], 
            data[constant.goal_end_date])
        tmp.id = count
        count += 1
        goal_list[tmp.id] = tmp
        goal_list_fields[tmp.id] = fields.Nested(goal_fields)
        return 
    
class Goal(Resource):

    @marshal_with(goal_fields)
    def get(self, id):
        try:
            return goal_list[int(id)]
        except:
            return abort(404)
    
    def patch(self, id):
        try:
            goal_list[int(id)] # for check what this goal is still in goal list
            data = json.loads(request.data)
            tmp = GoalModel(
                data[constant.goal_name], 
                data[constant.goal_target], 
                data[constant.goal_start_date], 
                data[constant.goal_end_date])
            tmp.id = id
            goal_list[int(id)] = tmp
        except:
            return abort(404)
        return
    
    def delete(self, id):
        try:
            goal_list[int(id)] # for check what this goal is still in goal list
            goal_list.pop(int(id))
            goal_list_fields.pop(int(id))
        except:
            return abort(404)
        return

