from flask import Flask, render_template, request, redirect, url_for, session, flash, json
from mongoengine import *
from models import *


connect('TodoList')

app = Flask(__name__)
app.secret_key = '1qaz0okm'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/service_register', methods=['POST'])
def service_register():
	email = request.form['email']
	password = request.form['password']
	confirmPassword = request.form['confirmPassword']
	if (password == confirmPassword):
			new_user = User(email=email, password=password)
			try:
				new_user.save()
			except NotUniqueError as e:
				return json.dumps({'status':'ERR','error':'Email already Registered'})
			else:
				return json.dumps({'status':'OK','email':email})
	else:
		return json.dumps({'status':'ERR','error':'Passwords dont match'})

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/service_login', methods=['POST'])
def service_login():
	email = request.form['email']
	password = request.form['password']
	db_users = User.objects(email=email)
	try:
		db_user = db_users[0]
	except IndexError:
		return json.dumps({'status':'ERR','error':'Email is not registered'})
	else:
		if (password == db_user.password):
			session['logged'] = True
			session['email'] = email
			return json.dumps({'status':'OK','email':email})
		else:
			return json.dumps({'status':'ERR','error':'Wrong Password'})


@app.route('/list')
def list():
	if(session['logged']):
		user_tasks = Task.objects(user=session['email'])
		return render_template('list.html', tasks = user_tasks, user_email=session['email'])
	else:
		return redirect(url_for('login'))

@app.route('/task/add', methods=['POST'])
def add():
	if (session['logged']):
		description = request.form['description']
		user = request.form['user']
		task = Task(status=0, description=description, user=user)
		task.save()
		return json.dumps({'status':'OK','msj':'Task Saved', 'id':str(task.id)})
	else:
		return json.dumps({'status':'ERR','error':'Session has expired'})


@app.route('/task/delete', methods=['POST'])
def delete():
	if (session['logged']):
		task_id = request.form['task_id']
		task = Task.objects(id=task_id)
		try:
			task.delete()
		except ValidationError:
			return json.dumps({'status':'ERR','error':'Task is not valid, or is already deleted'})
		else:
			return json.dumps({'status':'OK','msj':'Task Deleted'})
	else:
		return json.dumps({'status':'ERR','error':'Session has expired'})

@app.route('/task/update_status', methods=['POST'])
def update_status():
	if (session['logged']):
		task_id = request.form['task_id']
		task_status = request.form['status']
		task = Task.objects(id=task_id)
		try:
			task.modify(status=task_status)
		except ValidationError:
			return json.dumps({'status':'ERR','error':'Task is not valid, or is already deleted'})
		else:
			return json.dumps({'status':'OK','msj':'Task Status Updated'})
	else:
		return json.dumps({'status':'ERR','error':'Session has expired'})




if __name__ == "__main__":
    app.run(debug=True)

