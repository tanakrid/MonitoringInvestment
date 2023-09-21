from flask import Flask, render_template, jsonify, request
import json
from flask_restful import Resource, Api

from src.goal_manager import GoalManager
import src.goal_manager
import src.goal
app = Flask(__name__)
api = Api(app)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# --- REST api ---

@app.route('/greeting', methods = ['GET', 'POST'])
def home1():
    data = json.loads(request.data)
    data = f"{data['data']}, Nice to meet you"
    if (request.method == 'GET'):
        data = "hello world"
    return jsonify({'data': data})

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num**2})

# --- REST api with flask_restful ---

class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
        
        data = request.get_json()     # status code
        # return jsonify({'data': data}), 201
        return data
  
  
# another resource to calculate the square of a number
class Square(Resource):
  
    def get(self, num):
  
        return jsonify({'square': num**2})
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(GoalManager, '/goal_manager', '/goal_manager/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)