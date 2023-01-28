import sqlite3
open("db/users.db", 'w').close()
con = sqlite3.connect("db/users.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(id, email, firstname, lastname, password, token)")
cur.close()



open("db/posts.db", 'w').close()
con = sqlite3.connect("db/posts.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(id, message, current_dateTime)")
cur.close()



open("db/requests_friends.db", 'w').close()
con = sqlite3.connect("db/requests_friends.db")
cur = con.cursor()
cur.execute("CREATE TABLE req(id, id_to, status)")
cur.close()