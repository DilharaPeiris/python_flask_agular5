from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from testw import my_func



app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
# def hello():
#     return jsonify({'text':'Hello World!'})

#y_func()

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)       

x=my_func()

class TestData(Resource):
    def get(self):
        print('testData'+x)
        result = {'testData'}
        return x



api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(TestData, '/testData') # Route_4


if __name__ == '__main__':
   app.run(port=5002)