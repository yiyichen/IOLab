from app import myapp
from flask import request, abort, jsonify, make_response, render_template, redirect, json

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
    returned_object = {}
    returned_object['tasks'] = tasks
    print returned_object
    return json.dumps({'tasks': tasks})

@myapp.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task.get('id')==task_id:
            return json.dumps(task)
    return redirect(404)

@myapp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@myapp.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    print "tasks(0)"
    _list = []
    for task in tasks:
        _list.append(task.get('id'))
        # _list.append((tasks.index(task), task.get('id')))
    print max(_list)

    content = request.json
    if content.get('title') == None:
        return redirect(400)

    return_json = {
        "id": max(_list)+1,
        "title": content.get('title'),
        "description": content.get('description'),
        "done": False
    }

    return json.dumps(return_json)

@myapp.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request - make sure to specify a task title'}), 400)
