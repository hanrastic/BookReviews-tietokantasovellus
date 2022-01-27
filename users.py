
# from db import db
# from flask import abort, request, session
# from sqlalchemy import sql
# from werkzeug.security import check_password_hash, generate_password_hash

# def signup(username, password): #Role missing. To be added later
#     hash_value = generate_password_hash(password)
#     try:
#         sql = """INSERT INTO users (username, password, isAdmin)
#                 VALUES (:username, :password, :isAdmin)""" 
#         db.session.execute(sql, {"username":username, "password": hash_value, "isAdmin": False})#isAdmin == False
#         db.session.commit()
#     except:
#         return False

#     return login(username, password)

# def login(username, password):
#     sql = "SELECT id, password, isAdmin FROM users WHERE username=:username"
#     result = db.session.execute(sql, {"username": username})
#     user = result.fetchone()
#     if not user or not check_password_hash(user[1], password):
#         return False
#     return True