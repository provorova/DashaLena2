from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code = 302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <h1>web-сервер на flask</h1>

        <footer>
            &copy;Крамар Д.Н., Проворова Е.А., ФБИ-11, 3 курс, 2023   
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Крамар Д.Н., Проворова Е.А., Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности
        </div>

        <footer>
            &copy;Крамар Д.Н., Проворова Е.А., ФБИ-11, 3 курс, 2023   
        </footer>
    </body>
</html>
"""

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html style="background-color:rgb(210, 228, 248)">
<link rel="stylesheet" href="''' + url_for('static', filename = 'lab1.css') + '''">
    <head>
        <title>Крамар Д.Н., Проворова Е.А., Лабораторная 1</title>
    </head>
    <body>
        <h1 style="text-align: center; font-style:italic">Дуб</h1>
        <img src="''' + url_for('static', filename = 'oak.jpg') + '''">
    </body>
</html>
'''

