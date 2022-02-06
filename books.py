from distutils.log import ERROR
from tkinter import INSERT
from unittest import result
from markupsafe import re
from sqlalchemy import sql
from db import db

def create_a_review(user_id, book_id, book_comment):

    sql = ("INSERT INTO reviews "
            "(user_id, book_id, created_at, likes, rev_comment)"
            "VALUES "
            "(:user_id, :book_id, NOW(), :likes, :rev_comment)")
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
        return result.fetchone()[0] ##Tää feilaa jos kirjaa ei ole tietokannassa
    except KeyError: #Keksi tapa miten tää ei crashaa jos hakee book_id:tä kirjalle jota ei ole taulussa
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
    sql = "INSERT INTO ratings (book_id, book_rating) VALUES (:book_id, :rating)  ON CONFLICT DO NOTHING"
    db.session.execute(sql, {'book_id': book_id, 'rating': stars})
    db.session.commit()


def get_average_rating_for_book():
    try:
        sql = " "
    except KeyError:
        return False