from app import app
from flask import render_template, redirect, request, session
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
        categories = request.form.getlist('category')
        stars = request.form['stars']
        review_text = request.form['review-text']

        books.add_a_book(book_name)
        

        user_id = session["user_id"]
        book_id = books.get_a_book_id(book_name)

        books.insert_into_ratings(book_id, int(stars))
        
        for category in categories:
            category_id = books.get_category_id(category)
            books.insert_into_books_categories(book_id, category_id)

        books.create_a_review(user_id, book_id, review_text)

        return redirect("/")
    