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


@lab4.route("/lab4/fridge", methods = ['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template ('fridge.html')
    error = {}
    result = {}
    result2 = {}
    temp = request.form.get('temp')
    if temp == '' :
        error = 'Ошибка: не задана температура'
        result = ''
        result2 = ''
    elif int(temp) < -12 :
        result = 'Не удалось установить температуру - слишком низкое значение'
        result2 = ''
    elif int(temp) > -1 :
        result = 'Не удалось установить температуру - слишком высокое значение'
        result2 = ''
    elif -12 <= int(temp) <= -9:
        result = f'Установлена температура: {temp} °C'
        result2 = '***'
    elif -8 <= int(temp) <= -5:
        result = f'Установлена температура: {temp} °C'
        result2 = '**'
    else:
        result = f'Установлена температура: {temp} °C'
        result2 = '*'
    return render_template ('fridge.html', temp = temp, error=error, result=result, result2=result2)


@lab4.route("/lab4/zerno", methods = ['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template ('zerno.html')
    error = {}
    result = {}
    price = {}
    zerno = request.form.get('zerno')
    ves = request.form.get('ves')
    if zerno == 'ячмень':
        price = 12000
    elif zerno == 'овес':
        price = 8500
    elif zerno == 'пшеница':
        price = 8700
    else :
        price = 14000

    if ves == '' :
        error = 'Не введен вес'
    elif int(ves) <= 0 :
        error = 'Неверное значение веса'
    elif 50 <= int(ves) < 500:
        price = price * int(ves) * 0.9
        result = f'Сумма к оплате с учетом скидки 10% за большой объем: {price}'
    elif int(ves) >= 500 :
        error = 'Такого объема сейчас нет в наличии, заказ не может быть оформлен, укажите объем меньше'
    else:
        price = price * int(ves)
        result = f'Сумма к оплате: {price}'
    return render_template ('zerno.html', zerno=zerno, ves = ves, error=error, result=result)


@lab4.route("/lab4/cookies", methods = ['GET', 'POST'])
def cookies():
        if request.method == 'GET':
            return render_template ('cookies.html')
        
        color = request.form.get('color')
        headers = {
            'Set-Cookie': 'color=' + color + '; path=/',
            'Location': '/lab4/cookies'
        }
        return '', 303, headers