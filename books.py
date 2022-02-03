from tkinter import INSERT
from markupsafe import re
from sqlalchemy import sql
from db import db

def create_a_review(book_id, book_categories, book_rating, book_comment):
    ##print("Book addition: ",add_a_book(book_name))
    #print("Book: ", book_name, " ID: ",get_a_book_id(book_name))

    sql = ("INSERT INTO reviews "
            "(user_id, book_id, category_id, rating_id, created_at, likes, rev_comment)"
            "VALUES "
            )

    pass

def add_a_review_for_book():
    pass

def add_a_book(book_name):
    sql = ("INSERT INTO books " 
          "(name)"
          "VALUES "
          "(:name)")

    db.session.execute(sql, {'name': book_name})
    db.session.commit()

def get_a_book_id(book_name):
    try:
        sql = "SELECT id FROM books WHERE name=:book_name"
        result = db.session.execute(sql, {'book_name': book_name})
        return result.fetchone()
    except KeyError:
        return False
