from sqlalchemy import sql
from db import db


def create_a_review(user_id, book_id, book_comment):
    sql = ("INSERT INTO reviews "
            "(user_id, book_id, created_at, likes, rev_comment) "
            "VALUES "
            "(:user_id, :book_id, NOW(), :likes, :rev_comment) "
            "")
    db.session.execute(sql, {
        "user_id": user_id,
        "book_id": book_id,
        "likes": 0,
        "rev_comment":book_comment
    })
    db.session.commit()


def add_a_book(book_name):
    sql = "INSERT INTO books (name) VALUES (:name) ON CONFLICT DO NOTHING"

    db.session.execute(sql, {'name': book_name})
    db.session.commit()

def get_a_book_id(book_name):
    try:
        sql = "SELECT id FROM books WHERE name=:book_name"
        result = db.session.execute(sql, {'book_name': book_name})
        return result.fetchone()[0] 
    except KeyError: 
        return False

def get_category_id(category):
    try:
        sql = "SELECT id FROM categories WHERE name=:category"
        result = db.session.execute(sql, {'category': category})
        return result.fetchone()[0]
    except KeyError:
        return False

def insert_into_books_categories(book_id, category_id):
    sql = "INSERT INTO books_categories (book_id, category_id) VALUES (:book_id, :category_id) ON CONFLICT DO NOTHING"
    db.session.execute(sql, {'book_id': book_id, 'category_id': category_id})
    db.session.commit()

def insert_into_ratings(book_id, stars):
    sql = "INSERT INTO ratings (book_id, book_rating) VALUES (:book_id, :rating) ON CONFLICT DO NOTHING"
    db.session.execute(sql, {'book_id': book_id, 'rating': stars})
    db.session.commit()

def search_for_books_by_name(book_name):
    sql =  ("SELECT DISTINCT "
                "users.id, users.username, books.id, books.name, ratings.book_rating, reviews.created_at, reviews.likes, reviews.rev_comment "
            "FROM "
                "users "
            "INNER JOIN reviews ON users.id = reviews.user_id "
            "INNER JOIN books ON reviews.book_id = books.id "
            "INNER JOIN ratings ON books.id = ratings.book_id "
            "INNER JOIN books_categories ON ratings.id = books_categories.book_id "
            "WHERE LOWER(books.name) LIKE LOWER(:book_name) "
            "ORDER BY books.name")
    result = db.session.execute(sql, {'book_name': f'%{book_name}%'})
    return result.fetchall()

def search_for_books_by_category(book_categories):
    print(book_categories)

    sql = ( "SELECT DISTINCT "
                "users.id, users.username, books.id, books.name, ratings.book_rating, reviews.created_at, reviews.likes, reviews.rev_comment "
            "FROM "
                "users "
            "INNER JOIN reviews ON users.id = reviews.user_id "
            "INNER JOIN books ON reviews.book_id = books.id "
            "INNER JOIN ratings ON books.id = ratings.book_id "
            "INNER JOIN books_categories ON ratings.id = books_categories.book_id "
            "WHERE books_categories.category_id IN :book_category")
            
    result = db.session.execute(sql, {'book_category': book_categories})
    return result.fetchall()

def convert(list):
    return tuple(list)

def get_top_5_reviewed_books():
    sql =   ("SELECT "
            "books.name, ROUND(AVG(ratings.book_rating), 2) AS avg "
            "FROM books INNER JOIN ratings ON books.id = ratings.book_id "
            "GROUP BY books.name "
            "ORDER BY 2 DESC LIMIT 5")
    return db.session.execute(sql).fetchall()