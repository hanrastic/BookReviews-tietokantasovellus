from app import app
from flask import render_template, redirect, request, session
import users
import books

@app.route("/")
def index():
    #get top 5 reviewed books
    top_5_books = books.get_top_5_reviewed_books()
    return render_template("index.html", books = top_5_books)

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

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        request.args.get('query_by_name')
        query_by_name = request.args['query_by_name']
        print("Chosen to query by name")
        search_results = books.search_for_books_by_name(query_by_name)

        return render_template('result.html', results = search_results)

    if request.method == 'POST':
        print("Chosen to query by category")
        query_by_category = request.form.getlist('category')

        categories = []
        for category in query_by_category:
            categories.append(books.get_category_id(category))
        categories = books.convert(categories)

        search_results = books.search_for_books_by_category(categories)

        return render_template('result.html', results= search_results)

@app.route('/result/<string:name>/<float:avg>')
def result2(name, avg):
    print("Book Name: ", name, "AVG: ", avg)

    search_results = books.search_for_books_by_name(name)

    return render_template('result.html', results = search_results)



@app.route('/search')
def search():
    return render_template('search.html')

