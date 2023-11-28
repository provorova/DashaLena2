from flask import Blueprint, render_template, request
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "provorova_knowledge_base",
        password = "123")

    return conn;

def dbClose(cursor, connection):
    # закрываем курсор и соединение
    # порядок важен!
    cursor.close()
    connection.close()

@lab5.route("/lab5/")
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)      

    return "go to console"


@lab5.route("/lab5/users")
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    names = [row[1] for row in result]

    dbClose(cur, conn)

    return render_template('users.html', names = names)

