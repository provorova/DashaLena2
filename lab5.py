from flask import Blueprint, render_template, request
import psycopg2
lab5 = Blueprint('lab5', __name__)


@lab5.route("/lab5/")
def main():
    #параметры для подключения к БД
    conn = psycopg2.connect (
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "provorova_knowledge_base",
        password = "123"
    )
    # получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()

    # получаем курсор. спомощью него мы можем выполнять SQL-запросы
    cur.execute("SELECT * FROM users;")

    # fetchal - получить все строки, которые получились в результате
    # выполение SQL-запроса в execute 
    # созраняем эти строки в переменную result
    result = cur.fetchall()

    # закрываем соединение с БД
    cur.close()
    conn.close()

    print(result)

    return "go to console"

   
