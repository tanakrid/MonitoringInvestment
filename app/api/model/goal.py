from flask_restful import fields

goal_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'target': fields.Integer,
    'start_date': fields.String,
    'end_date': fields.String,
    'progress': fields.Float
}

class Goal:
    
    def __init__(self, name, target, start_date = None, end_date = None):
        self.id = ""
        self.name = name
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.progress = 0
    
