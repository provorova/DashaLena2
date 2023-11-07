from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route("/lab4/")
def lab():
    return render_template ('lab4.html')


@lab4.route("/lab4/login", methods = ['GET', 'POST'])
def login():
    errors = {}
    if request.method == 'GET':
        return render_template ('login.html', errors = errors)

    username = request.form.get('username')
    if username == '':
        errors['username'] = 'Не введен логин'
    password = request.form.get('password')
    if password == '':
        errors['password'] = 'Не введен пароль'
    if username == 'alex' and password == '123':
        return render_template ('succes4.html', username = username)
    
    error = 'Неверные логин и/или пароль'
    return render_template ('login.html', username = username, 
                            password = password, errors = errors, error = error)