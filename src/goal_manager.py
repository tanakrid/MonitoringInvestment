from goal import Goal
import json
from flask_restful import Resource
from flask import jsonify, request

class GoalManager(Resource):

    def __init__(self):
        super().__init__()
        self.goal_repository = {}
        self.count = 0

    def get(self):
        return jsonify({ 'data': self.goal_repository })
    
    def get(self, id):
        return jsonify({ 'data': self.goal_repository[id] })
    
    def post(self):
        data = json.loads(request.data)
        tmp = Goal(data['name'], data['target'], data['start_date'], data['end_date'])
        tmp.id = self.count
        self.count += 1
        self.goal_repository[tmp.id] = tmp
        return
    
    def patch(self, id):
        data = json.loads(request.data)
        tmp = Goal(data['name'], data['target'], data['start_date'], data['end_date'])
        tmp.id = id
        self.goal_repository[id] = tmp
        return
    
    def delete(self, id):
        self.goal_repository.pop(id)
        return

