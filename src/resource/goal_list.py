from ..model.goal import Goal as GoalModel, goal_fields
from ..util import constant, validate

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
        try:
            global count
            data = json.loads(request.data)
            tmp = validate.validate_input_post_goal(data)
            tmp.id = count
            count += 1
            goal_list[tmp.id] = tmp
            goal_list_fields[tmp.id] = fields.Nested(goal_fields)
        except Exception as e:
            return abort(403, "Invalid input parameter")
    
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
            tmp = validate.validate_input_post_goal(data)
            tmp.id = id
            goal_list[int(id)] = tmp
        except KeyError:
            return abort(404)
        except Exception:
            return abort(403, "Invalid input parameter")
    
    def delete(self, id):
        try:
            goal_list[int(id)] # for check what this goal is still in goal list
            goal_list.pop(int(id))
            goal_list_fields.pop(int(id))
        except:
            return abort(404)
