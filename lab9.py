from flask import Blueprint, render_template, request

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error.html'), 404

@lab9.route('/lab9/500')
def server_error():
    return render_template('lab9/error2.html'), 500


@lab9.route('/lab9/greeting_card', methods=['GET', 'POST'])
def greeting_card():
    if request.method == 'POST':
        sender_name = request.form['sender_name']
        recipient_name = request.form['recipient_name']
        recipient_gender = request.form['recipient_gender']
        # Здесь вы можете создать свою открытку, используя данные из формы, например:
        if recipient_gender == 'male':
            greeting = f"С Новым Годом, {recipient_name}! Желаю быть счастливым! С наилучшими пожеланиями, {sender_name}."
        else:
            greeting = f"С Новым Годом, {recipient_name}! Желаю быть счастливой! С наилучшими пожеланиями, {sender_name}."
        return render_template ('/lab9/card.html', greeting=greeting)
    else:
        # Если это GET запрос, то выводим форму для ввода данных
        return render_template('/lab9/form.html') 