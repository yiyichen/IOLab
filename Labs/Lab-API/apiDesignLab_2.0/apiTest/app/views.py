from app import myapp
from flask import request, abort, jsonify, make_response, render_template, redirect
import requests
from pprint import pprint

@myapp.route('/')
@myapp.route('/index')
def index():
	return render_template('base.html', data='Click one of the above links to test your API!')

@myapp.route('/get-all-tasks')
def get_all_tasks():
    pprint('------- GETTING ALL TASKS -------')

    response = requests.get('http://localhost:5000/todo/api/v1/tasks')
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=response.text)

@myapp.route('/get-task-by-id')
def get_task_by_id(task_id=1):
    pprint('------- GETTING TASK -------')

    task_id = task_id
    if type(task_id) == int or int(task_id):
        task_id = str(task_id)
    else:
        pprint('------- ERROR - PLEASE SPECIFY TASK NUMBER AS INT -------')

    response = requests.get('http://localhost:5000/todo/api/v1/tasks/'+task_id)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=response.text)

@myapp.route('/get-task-by-id-error')
def get_task_by_id_error(task_id=100):
    pprint('------- GETTING TASK -------')

    task_id = task_id
    if type(task_id) == int or int(task_id):
        task_id = str(task_id)
    else:
        pprint('------- ERROR - PLEASE SPECIFY TASK NUMBER AS INT -------')

    response = requests.get('http://localhost:5000/todo/api/v1/tasks/'+task_id)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=response.text)

@myapp.route('/create-new-task')
def create_new_task():
    pprint('------- CREATING TASK -------')

    title = 'New Task'

    data = {
    'title': title,
    'description': ''
    }

    response = requests.post('http://localhost:5000/todo/api/v1/tasks', json=data)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=response.text)


@myapp.route('/create-new-task-error')
def create_new_task_error():
    pprint('------- CREATING TASK -------')

    data = {
    'description': ''
    }

    response = requests.post('http://localhost:5000/todo/api/v1/tasks', json=data)
    decodedResponse = response.json()
    pprint(decodedResponse)
    return render_template('base.html', data=response.text)