from flask import Flask
from flask import render_template, request, redirect, session
import sqlite3
import db
import config, users
import postBoard

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            return redirect("/home")
        else:
            return "VIRHE: Virheellinen käyttäjätunnus tai salasana"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return "VIRHE: Salasanat eivät täsmää"
        try:
            users.create_user(username, password1)
            return redirect("/login")
        except sqlite3.IntegrityError:
            return "VIRHE: Käyttäjätunnus on jo käytössä"

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect("/login")
    posts = postBoard.get_posts()
    return render_template("home.html", posts=posts)

@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        user_id = session["user_id"]
        postBoard.add_post(title, content, user_id)
        return redirect("/home")