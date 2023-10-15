from project.api.model.goal import Goal as GoalModel, goal_fields
from project import db
from project.api.util import validate

from flask_restful import Resource, marshal_with, reqparse
from flask import abort

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('target', type=int, required=True)
parser.add_argument('start_date', type=str, required=True)
parser.add_argument('end_date', type=str, required=True)

class GoalList(Resource):

    @marshal_with(goal_fields)
    def get(self):
        return GoalModel.query.all()
    
    @marshal_with(goal_fields)
    def post(self):
        args = parser.parse_args()
        goal = None
        try:
            goal = validate.validate_input_post_goal(args)
        except Exception:
            return abort(403, "Invalid input parameter")
        db.session.add(goal)
        db.session.commit()
        return goal
    
class Goal(Resource):

    @marshal_with(goal_fields)
    def get(self, id):
        goal = GoalModel.query.get(id)
        if not goal:
            return abort(404)
        return goal
    
    @marshal_with(goal_fields)
    def patch(self, id):
        args = parser.parse_args()
        goal = GoalModel.query.filter_by(id=id).first()
        if not goal:
            return abort(404, 'Goal not found!')
        try:
            tmp = validate.validate_input_post_goal(args)

            # bind data from args to existing data
            goal.id = id
            goal.name = tmp.name
            goal.target = tmp.target
            goal.start_date = tmp.start_date
            goal.end_date = tmp.end_date
            goal.progress = tmp.progress

            db.session.commit()
        except Exception:
            return abort(403, "Invalid input parameter")
        return goal
    
    @marshal_with(goal_fields)
    def delete(self, id):
        goal = GoalModel.query.get(id)
        if not goal:
            return abort(404, 'Goal not found!')
        db.session.delete(goal)
        db.session.commit()