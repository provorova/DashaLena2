from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code = 302)


@lab1.route("/menu")
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

        <h2>Список лабораторных работ</h2>

        <ul>
            <li><a href="/lab1">Лабораторная работа 1</a></li>
            <li><a href="/lab2">Лабораторная работа 2</a></li>
        </ul>

        <footer>
            &copy;Крамар Д.Н., Проворова Е.А., ФБИ-11, 3 курс, 2023   
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1")
def lab():
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

        <a href="/menu">menu</a>

        <h2>Реализованные роуты</h2>

        <ul>
            <li><a href="/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="/lab1/student">/lab1/student - студент</a></li>
            <li><a href="/lab1/python">/lab1/python - python</a></li>
            <li><a href="/lab1/winx">/lab1/winx - винкс</a></li>
        </ul>

        <footer>
            &copy;Крамар Д.Н., Проворова Е.А., ФБИ-11, 3 курс, 2023   
        </footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
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
        <img id="oak" src="''' + url_for('static', filename = 'oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html style="background-color:MistyRose">
<link rel="stylesheet" href="''' + url_for('static', filename = 'lab1.css') + '''">
    <head>
        <title>Крамар Д.Н., Проворова Е.А., Лабораторная 1</title>
    </head>
    <body>
        <h1 id="fam">Крамар Дарья Николавена, Проворова Елена Андреевна</h1>
        <img id="st" src="''' + url_for('static', filename = 'logo.png') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename = 'lab1.css') + '''">
    <head>
        <title>Крамар Д.Н., Проворова Е.А., Лабораторная 1</title>
    </head>
    <body>
        <div class="p" style="color:rgb(56, 116, 181)">
            Язык Python является, пожалуй, самым простым в изучении и самым
            приятным в использовании из языков программирования, получивших 
            широкое распространение. Программный код на языке Python
            легко читать и писать, и, будучи лаконичным, он не выглядит 
            загадочным. Python – очень выразительный язык, позволяющий уместить
            приложение в меньшее количество строк, чем на это потребовалось бы
            в других языках, таких как C++ или Java.
        </div>

        <div class="p" style="color:rgb(255, 170, 29)">
            Python является кросс-платформенным языком: обычно одна и та же
            программа на языке Python может запускаться и в Windows, и в UNIX-
            подобных системах, таких как Linux, BSD и Mac OS, для чего достаточно 
            просто скопировать файл или файлы, составляющие программу, на
            нужный компьютер; при этом даже не потребуется выполнять «сборку»,
            или компилирование программы. Конечно, можно написать на
            языке Python программу, которая будет использовать некоторые 
            характерные особенности конкретной операционной системы, но такая
            необходимость возникает крайне редко, т. к. практически вся 
            стандартная библиотека языка Python и большинство библиотек сторонних 
            производителей обеспечивают полную кросс-платформенность.
        </div>
        <img id="py" src="''' + url_for('static', filename = 'python.png') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/winx')
def winx():
    return '''
<!doctype html>
<html style="background-color:rgb(20, 41, 98)">
<link rel="stylesheet" href="''' + url_for('static', filename = 'lab1.css') + '''">
    <head>
        <title>Крамар Д.Н., Проворова Е.А., Лабораторная 1</title>
    </head>
    <body>
        <div class="w">
            В волшебном мире Магикс есть школа Алфея, где юных фей обучают магическим навыкам. 
            Пять учениц этой школы не только ходят в кафе после уроков и встречаются с мальчиками, 
            но и защищают свою планету от зла. Каждая из фей обладает особенным характером. 
            Техна может разобраться с любой электроникой, тихая и застенчивая Флора любит растения, 
            Муза – настоящая меломанка, блондинка Стела – наследная принцесса планеты Солярия, 
            а Блум является признанным лидером в этой компании. Клуб Винкс был создан феями 
            в знак вечной дружбы и взаимной помощи. У каждой юной волшебницы есть 
            миниатюрные помощницы – пикси.
        </div>

        <div class="w">
            Жизнь участниц Клуба Винкс была бы простой и беззаботной, если 
            бы не злые Айси, Дарси и Сторми, три ведьмы из Клуба Трикс, которые 
            пытаются подчинить себе мир. Их козни доставят немало хлопот феям, 
            но только искренняя дружба и взаимовыручка поможет Клубу Винкс победить зло.
        </div>
        <img id="wi" src="''' + url_for('static', filename = 'winx.jpg') + '''">
    </body>
</html>
'''

