from app import myapp
from flask import request, abort, jsonify, make_response, render_template, redirect

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@myapp.route('/')
@myapp.route('/todo/api')
def index():
	return render_template('api.html')

@myapp.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
	pass

@myapp.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    pass

@myapp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@myapp.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    pass

@myapp.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request - make sure to specify a task title'}), 400)