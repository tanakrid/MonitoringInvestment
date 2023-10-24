from project.api.model.user import User
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
import project.api.util.constant as constant
from project import db

def authenticate(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return user

def identity(payload):
    user_id = payload
    return User.query.filter_by(id=user_id).first()

parser = reqparse.RequestParser()
parser.add_argument(constant.login_username, help='This field cannot be blank', required=True)
parser.add_argument(constant.login_password, help='This field cannot be blank', required=True)

class Register(Resource):
    def post(self):
        data = parser.parse_args()
        exist_user = User.query.filter_by(username=data[constant.login_username]).first()
        if not exist_user:
            new_user = User(
                username=data[constant.login_username],
                password=data[constant.login_password],
                role=constant.login_role_normal 
            )
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity=new_user.id)
            return {'message': 'User {} was created'.format(data[constant.login_username]), 'access_token': access_token}
        else:
            return {'message': 'User {} was already have to used'.format(data[constant.login_username])}, 401

class Login(Resource):
    def post(self):
        data = parser.parse_args()
        user = authenticate(data[constant.login_username], data[constant.login_password])
        if user:
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
        
blacklist = set()
class Logout(Resource):
    @jwt_required
    def post(self):
        jti = get_jwt()["jti"]
        blacklist.add(jti)
        return {"msg": "Successfully logged out"}

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        print(get_jwt_identity())
        current_user = identity(get_jwt_identity())
        return {'id': current_user.id, 'username': current_user.username}, 200


