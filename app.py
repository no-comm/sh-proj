from flask import Flask, request, render_template, redirect, url_for, flash
import connect_db as db
from hashlib import sha256
token = ""
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=["GET"])
def home():
    return redirect("login")

@app.route('/', methods=['POST'])
def posting():
    return redirect("login")

@app.route('/login', methods=["GET"])
def login_get():
    return render_template('Вход.html')
@app.route('/login', methods=["POST"])
def login_post():
    try:
        if db.get_user(request.form["email"])[0][4] == sha256(request.form['password'].encode("utf-8")).hexdigest():
            global token
            token = db.get_token(request.form['email'])
            return redirect("/main")
        else:
            return render_template("Вход_error.html")
    except:return render_template("Вход_error.html")
@app.route('/register', methods=["GET"])
def register_get():
    return render_template('Регистрация.html')
@app.route('/register', methods=["POST"])
def register_post():
    try:
        if db.get_user(request.form["email"]) == []:
            db.add_user(request.form['email'], request.form['firstname'],request.form['lastname'],  request.form['password'])
            global token
            token = db.get_token(request.form['email'])
            return redirect("main")
        elif not db.get_user(request.form["email"]) == []:
            return render_template("Регистрация_error.html")
        else:
            return redirect("404")
    except:return render_template("Регистрация_error.html")
@app.route('/main', methods=["GET"])
def main_page():
    global token
    flash(token)
    return render_template("Моя-страница.html")
@app.route('/friends', methods=["GET"])
def friends():
    return render_template("Друзья.html")
@app.route('/add_friends', methods=["POST"])
def add_friends_post():
    if request.data.decode():
        data = request.data.decode().split(",")
        db.req_friend(data[0], data[1], "0")
        return "True"
@app.route('/accept_friends', methods=["POST"])
def accept_friends_post():
    if request.data.decode():
        data = request.data.decode().split(",")
        db.req_friend(data[0], data[1], 1)
        return "True"
@app.route('/friends', methods=["POST"])
def friends_post():
    if request.data:
        humans = db.give_human(request.data.decode())
        return humans
    return "False"


@app.route('/my_friend', methods=["POST"])
def my_friend_post():
    if request.data:
        return db.give_friend(request.data.decode())
    return "False"


@app.route('/del_friend', methods=["POST"])
def del_friend_post():
    if request.data:
        data = request.data.decode().split(",")
        db.del_friend(data[0], data[1])
        return "true"
    return "False"


@app.route('/my_friend', methods=["GET"])
def my_friend():
    return render_template("Мои друзья.html")


@app.route('/im', methods=["GET"])
def im():
    return render_template("Месседжер.html")
@app.route('/news', methods=["GET"])
def news():
    return render_template("Новости.html")
@app.route('/logout', methods=["GET"])
def logout():
    return redirect("/")
@app.route('/settings', methods=["GET"])
def settings():
    return render_template("Настройки.html")
@app.route('/get_username', methods=["POST"])
def get_username():
    post = request.data.decode()
    if post:
        return [db.get_user(id=post)[0][2], db.get_user(id=post)[0][3]]
    else:
        return "None"

@app.route('/get_my_id', methods=["POST"])
def get_my_id():
    post = request.data.decode()
    if post:
        return db.get_user(token=post)[0][0]
    else:
        return "None"
@app.route('/wall_post', methods=["POST"])
def wall_post():
    post = request.data.decode()
    return db.wall_post()
@app.route('/add_post', methods=["POST"])
def add_post():
    post = request.data.decode().split("|")
    id = db.add_post(post[0], post[1])
    return "True"
@app.route('/get_posts', methods=["POST"])
def get_posts():
    id = request.data.decode()
    return db.get_posts(id)
@app.route('/user', methods=["POST"])
def user():
    id = request.data.decode()
    urls = ["main", "login", "friends", "register", "im", "news", "logout", "settings", "add_post", "get_posts", "user", "404"]
    for i in urls:
        if i == id:
            return "False"
    check = db.get_user(id=id)
    if len(check) != 0:
        return "True"
    else:
        return "False"
    
@app.route('/404', methods=["GET"])
def error_404():
    return render_template("404.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template("12312312.html")