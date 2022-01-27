import users
from os import getenv
from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        #users.signup(username, password)
        signup(username, password)
        return redirect("/login")



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.ht ml')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #Here check if credentials are correct
            #If not, return error.html
        return redirect('/')

def signup(username, password): #Role missing. To be added later
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password, isAdmin)
                VALUES (:username, :password, :isAdmin)""" 
        db.session.execute(sql, {"username":username, "password": hash_value, "isAdmin": False})#isAdmin == False
        db.session.commit()
    except:
        return False

    return login(username, password)

def login(username, password):
    sql = "SELECT id, password, isAdmin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user or not check_password_hash(user[1], password):
        return False
    return True