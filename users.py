from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password, is_admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[1], password):
        return False
    
    session['username'] = username
    session['user_id'] = user[0]
    session['role'] = user[2]

    return True

def logout():
    del session['user_id']
    del session['username']
    del session['role']

def signup(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password, is_admin)
                VALUES (:username, :password, :is_admin)""" 
        db.session.execute(sql, {"username":username, "password": hash_value, "is_admin": False})#isAdmin == False
        db.session.commit()
    except:
        return False

    return login(username, password)

def get_current_user():
    try:
        user_id = session['user_id']

        sql = "SELECT username, is_admin FROM users WHERE id=:user_id"
        result = db.session.execute(sql, {'user_id': user_id})
        return result.fetchone()
    except KeyError:
        return False
