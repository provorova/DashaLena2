from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
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
def lab():
    return render_template ('lab5.html')

@lab5.route("/lab5/glavn")
def glavn():
    visibleUser = "Anon"
    
    if 'username' in session:  
        visibleUser = session['username']  

    return render_template('glavn.html', username = visibleUser)


@lab5.route("/lab5/users")
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    names = [row[1] for row in result]

    dbClose(cur, conn)

    return render_template('users.html', names = names)


@lab5.route("/lab5/register", methods=["GET", "POST"])
def registerPage():
    errors = {}

    visibleUser = "Anon"
    
    if 'username' in session:  
        visibleUser = session['username']

    if request.method == "GET":
        return render_template("register.html", username=visibleUser)

    username = request.form.get("username")
    password = request.form.get("password")

    if username == '' or password == '':
        errors = "Пожалуйста, заполните все поля"
        return render_template("register.html", errors=errors, username=visibleUser)

    hashPassword = generate_password_hash(password)
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;", (username,
    ))
    
    if cur.fetchone() is not None:
        errors = "Пользователь с данным именем уже существует"
        dbClose(cur, conn)
        return render_template("register.html", errors=errors, username=visibleUser)

    cur.execute(f"INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")


@lab5.route("/lab5/login", methods=["GET", "POST"])
def loginPage():
    errors = []; 

    visibleUser = "Anon"
    
    if 'username' in session:  
        visibleUser = session['username']

    if request.method == "GET":
        return render_template("loginn.html", username=visibleUser)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if username == '' or password == '':
        errors  = 'Пожалуйста, заполните все поля'
        return render_template("loginn.html", errors=errors, username=visibleUser)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))    

    result = cur.fetchone()

    if result is None:
        errors = "Неправильный логин или пароль"
        dbClose(cur, conn)
        return render_template("loginn.html", errors=errors, username=visibleUser)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5/glavn")
    else:
        errors = 'Неправильный логин или пароль'
        return render_template("loginn.html", errors=errors, username=visibleUser)


@lab5.route("/lab5/new_article", methods=["GET", "POST"])
def createArticle():
    errors = []
    userID = session.get("id")
    visibleUser = "Anon"
    
    if 'username' in session:  
        visibleUser = session['username']

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html", username=visibleUser)
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors = "Заполните текст"
                return render_template("new_article.html", errors=errors, username=visibleUser)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles(user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, text_article))

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")

    return redirect("/lab5/login")  


@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):
 
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and (user_id = %s or is_public = %s) ", (article_id, userID, 'True'))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"

        text = articleBody[1].splitlines()

        return render_template("articleN.html", article_text=text, article_title=articleBody[0], username=session.get("username"))


@lab5.route("/lab5/user_articles")
def user_articles():

    userID = session.get("id")
    
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, title, is_public FROM articles WHERE user_id = %s", (userID,))

        result = cur.fetchall()

        dbClose(cur, conn)

        return render_template('user_articles.html', result=result, username=session.get("username"))
    
    return redirect("/lab5/login")


@lab5.route("/lab5/publish", methods=["POST"])
def publish():

    articleID = request.form["article_id"]
    conn = dbConnect()
    cur = conn.cursor()
    
    cur.execute("SELECT is_public FROM articles WHERE id = %s", (articleID,))
    status = cur.fetchone()[0]
    
    new_status = not status

    cur.execute("UPDATE articles SET is_public = %s WHERE id = %s", (new_status, articleID))
    conn.commit()
    dbClose(cur, conn)
    
    return redirect("/lab5/user_articles")


@lab5.route("/lab5/articles")
def articles():
    userID = session.get("id")
    
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, title, COALESCE(array_length(likes, 1), 0) as likes_count FROM articles WHERE is_public = %s and %s=ANY(is_favorite);", (True, userID))
        result1 = cur.fetchall()

        cur.execute("SELECT id, title, COALESCE(array_length(likes, 1), 0) as likes_count FROM articles WHERE is_public = %s AND (%s!=ALL(is_favorite) OR is_favorite IS NULL);", (True, userID))
        result2 = cur.fetchall()

        dbClose(cur, conn)

        return render_template('articles.html', result1=result1, result2=result2, username=session.get("username"))
    
    return redirect("/lab5/login")


@lab5.route("/lab5/favorite", methods=["POST"])
def fovorite():

    articleID = request.form["article_id"]
    userID = session.get("id")
    conn = dbConnect()
    cur = conn.cursor()
    
    cur.execute("SELECT is_favorite FROM articles WHERE id = %s", (articleID,))
    favorite = cur.fetchone()[0]
    
    if favorite is not None:
        if userID in favorite:
            favorite.remove(userID)
        else:
            favorite.append(userID)
    else:
        favorite = [userID] 

    cur.execute("UPDATE articles SET is_favorite = %s WHERE id = %s", (favorite, articleID))

    conn.commit()
    dbClose(cur, conn)
    
    return redirect("/lab5/articles")


@lab5.route("/lab5/like", methods=["POST"])
def like():

    articleID = request.form["article_id"]
    userID = session.get("id")
    conn = dbConnect()
    cur = conn.cursor()
    
    cur.execute("SELECT likes FROM articles WHERE id = %s", (articleID,))
    like = cur.fetchone()[0]
    
    if like is not None:
        if userID in like:  
            like.remove(userID)
        else:
            like.append(userID)
    else:
        like = [userID] 

    cur.execute("UPDATE articles SET likes = %s WHERE id = %s", (like, articleID))

    conn.commit()
    dbClose(cur, conn)
    
    return redirect("/lab5/articles")

@lab5.route("/lab5/exit")
def exit():
    
    session.clear()

    return redirect('/lab5/glavn')

