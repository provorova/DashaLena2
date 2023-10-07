from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


@app.route("/lab2/example")
def example():
    name, nomer_gr, nomer_lab, nomer_k = 'Крамар Дарья, Проворова Елена', 'ФБИ-11', 2, '3 курс'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321},
        ]
    books = [
        {'avtor': 'Лев Толстой','name':'Война и мир', 'zanr': 'роман-эпопея', 'stran': 1300 },
        {'avtor': 'Джеймс Джойс','name':'Улисс', 'zanr': 'роман', 'stran': 1056 },
        {'avtor': 'Александр Солженицын','name':'Архипелаг Гулаг', 'zanr': 'автобиография', 'stran': 564 },
        {'avtor': 'Джейн Остин','name':'Предубеждение и гордость', 'zanr': 'роман', 'stran': 448 },
        {'avtor': 'Вирджиния Вулф','name':'На маяк', 'zanr': 'роман', 'stran': 140 },
        {'avtor': 'Маргарет Митчилл','name':'Унесенные ветром', 'zanr': 'роман', 'stran': 780 },
        {'avtor': 'Карл Маркс','name':'Капитал', 'zanr': 'марксизм', 'stran': 962 },
        {'avtor': 'Уолт Уитмен','name':'Листья травы', 'zanr': 'поэзия', 'stran': 432 },
        {'avtor': 'Джордж Оруэлл','name':'Скотный двор', 'zanr': 'притча', 'stran': 100 },
        {'avtor': 'Натанаэл Уэст','name':'День саранчи', 'zanr': 'роман', 'stran': 256 },
        ]
    return render_template ('example.html', name=name, nomer_gr=nomer_gr, 
                            nomer_lab=nomer_lab, nomer_k=nomer_k, fruits=fruits, books=books)

@app.route("/lab2/")
def lab2():
    return render_template ('lab2.html')

@app.route("/lab2/flowers")
def flowers():
    return render_template ('flowers.html')

@app.route("/lab2/zachita")
def zachita():
    A = 1.2
    B = 2
    C = 3

    N = 5
    K = 5

    sum = 0
    for i in range(N):
        sum += i**K

    return render_template ('zachita.html', A=A, B=B, C=C, N=N, K=K, sum=sum)