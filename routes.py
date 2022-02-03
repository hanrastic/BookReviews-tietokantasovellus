#Module for handling html and pagrequests
from crypt import methods
from app import app
from flask import render_template, redirect, request
import users
import books

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
        if users.signup(username, password):
            return redirect("/")
        else:
            return redirect("/login")



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect('/')

@app.route('/logout')
def logout():
    users.logout()
    return redirect('/')

@app.route('/createreview', methods=['GET', 'POST'])
def create_review():
    if request.method == 'GET':
        return render_template('createreview.html')
    if request.method == 'POST':
        book_name = request.form['book_name']
        categories = request.form.getlist("category")
        stars = request.form['stars']
        review_text = request.form['review-text']
        print(book_name, categories, stars, review_text)

        if not books.get_a_book_id(book_name): #If book is NOT in db
            books.add_a_book(book_name)

        book_id = books.get_a_book_id(book_name)

        books.create_a_review(book_id, categories, stars, review_text)

        return redirect("/")
    