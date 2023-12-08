from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2
from Db import db
from Db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__)

@lab6.route("/lab6/")
def lab():
    return render_template ('lab6.html')

@lab6.route("/lab6/checkusers")
def userss():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route("/lab6/checkarticles")
def articless():
    articless = articles.query.all()
    print(articless)
    return "result in console!"


@lab6.route("/lab6/glavn")
def glavn():
    visibleUser = "Anon"
    if current_user is not None:
        visibleUser = current_user.username

    if 'username' in session:  
        visibleUser = session['username']  

    return render_template('glavn.html', username = visibleUser)


@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():

    errors = {}

    if request.method == "GET":
        return render_template("register.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if username_form == '' or password_form == '':
        errors = "Пожалуйста, заполните все поля"
        return render_template("register.html", errors=errors)

    if len(password_form) < 5:
        errors = "Пароль не должен быть меньше 5-ти символов"
        return render_template("register.html", errors=errors)

    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        errors = 'Пользватель с таким именем уже существует'
        return render_template("register.html", errors=errors)

    hashedPswd = generate_password_hash(password_form, method='pbkdf2')

    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)

    db.session.commit()

    return redirect("/lab6/login")


@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("loginn.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if username_form == '' or password_form == '':
        errors = "Пожалуйста, заполните все поля"
        return render_template("loginn.html", errors=errors)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect("/lab6/articles")
        else:
            errors = "Неправильный пароль"
            return render_template("loginn.html", errors=errors)
    else:
        errors = "Пользователь не сущетсвует"
        return render_template("loginn.html", errors=errors)
    

@lab6.route("/lab6/user_articles")
@login_required
def articles_list():
    visibleUser = current_user.username
    # select * from articles where user_id = current_user.id
    my_articles = articles.query.filter_by(user_id=current_user.id)
    return render_template("user_articles.html", articles=my_articles, username=visibleUser)


@lab6.route("/lab6/new_article", methods=["GET", "POST"])
@login_required
def createArticle():
    visibleUser = current_user.username

    errors = []

    if request.method == "GET":
            return render_template("new_article.html", username=visibleUser)
        
    if request.method == "POST":
        text_article = request.form.get("text_article")
        title = request.form.get("title_article")

        if len(text_article) == 0:
            errors = "Заполните текст"
            return render_template("new_article.html", errors=errors, username=visibleUser)

        new = articles(user_id=current_user.id, title=title, text_article=text_article)
        db.session.add(new)
        db.session.commit()

        return redirect(f"/lab6/articles/{new.id}")


@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def getArticle(article_id):
    visibleUser = current_user.username

    articleBody = articles.query.filter_by(id=article_id).all()

    if articleBody is None:
        return "Not found!"

    text = articleBody[1].splitlines()

    return render_template("articleN.html", article_text=text, article_title=articleBody[0], username=visibleUser)


@lab6.route("/lab6/publish", methods=["POST"])
def publish():
    article_id = request.form["article_id"]
    article = Article.query.get(article_id)

    article.is_public = not article.is_public
    db.session.commit()

    return redirect("/lab6/user_articles")


@lab6.route("/lab6/articles")
@login_required
def list_articles():
    visibleUser = current_user.username

    result1 = (
        db.session.query(articles.id, articles.title, db.func.coalesce(db.func.array_length(articles.likes, 1), 0).label('likes_count'))
        .filter(articles.is_public == True)
        .filter(articles.is_favorite.any(current_user.id))
        .all()
    )

    result2 = (
        db.session.query(articles.id, articles.title, db.func.coalesce(db.func.array_length(articles.likes, 1), 0).label('likes_count'))
        .filter(articles.is_public == True)
        .filter(
            ~articles.is_favorite.any(current_user.id) | (articles.is_favorite.is_(None))
        )
        .all()
    )


    return render_template('articles.html', result1=result1, result2=result2, username=current_user.username)

@lab6.route("/lab6/favorite", methods=["POST"])
def fovorite():

    articleID = request.form["article_id"]
    article = articles.query.get(articleID)
    if current_user.id in article.is_favorite:
        article.is_favorite.remove(current_user.id)
    else:
        article.is_favorite.append(current_user.id)
    db.session.commit()

    return redirect("/lab6/articles")
    

@lab6.route("/lab6/like", methods=["POST"])
def like():

    articleID = request.form["article_id"]
    article = articles.query.get(articleID)

    if current_user.id in article.likes:
        article.likes.remove(current_user.id)
    else:
        article.likes.append(current_user.id)
    db.session.commit()

    return redirect("/lab6/articles")


@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6")
