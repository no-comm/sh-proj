import sqlite3
import random
import string
from hashlib import sha256
import datetime
def give_last_id():
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    sql2= '''SELECT * FROM users ORDER BY id;'''
    try:
        if cur.execute(sql2).fetchall()[-1][0]:
            return cur.execute(sql2).fetchall()[-1][0]
        else:
            return "0"
    except:
        return "0"
def get_token(email: str):
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    return cur.execute("SELECT * FROM users WHERE email=(?)", [email]).fetchall()[0][-1]

def add_user(email: str, firstname: str, lastname: str, password: str):
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    sql = ''' INSERT INTO users
            VALUES(?,?,?,?,?,?) '''
    id = int(give_last_id()) + 1
    token = ''.join(random.choices(string.ascii_letters, k = 20))
    cur.execute(sql, [str(id), email, firstname, lastname, sha256(password.encode("utf-8")).hexdigest(), token])
    con.commit()



def del_user(id: str):
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    sql = 'DELETE FROM users WHERE id=(?)'
    cur.execute(sql, [id])
    con.commit()


def get_user(email: str = None, token: str = None, id: str = None) -> []:
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    if not email is None:
        res = cur.execute("SELECT * FROM users WHERE email=(?)", [email]).fetchall()
        return res
    if not token is None:
        res = cur.execute("SELECT * FROM users WHERE token=(?)", [token]).fetchall()
        return res
    if not id is None:
        res = cur.execute("SELECT * FROM users WHERE id=(?)", [id]).fetchall()
        return res
    if email and token and id is None:
        return "No"

def add_post(token: str, message: str):
    id = get_user(token=token)[0][0]
    current_dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    con = sqlite3.connect("db/posts.db")
    cur = con.cursor()
    sql = ''' INSERT INTO users
            VALUES(?,?,?) '''
    cur.execute(sql, [id, message, current_dateTime])
    con.commit()

def get_posts(id: str):
    con = sqlite3.connect("db/posts.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users WHERE id=(?)", [id]).fetchall()
    posts = []
    for i in res:
        posts.append(i[1])
    return posts
def give_human(inp: str):
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users").fetchall()
    len_ = len(inp)
    humans = {}
    for i in res:
        firstname_ = i[2]
        lastname_ = i[3]
        if inp == firstname_[:len_]:
            humans[firstname_+" "+lastname_] = i[0]
        elif inp == lastname_[:len_]:
            humans[firstname_+" "+lastname_] = i[0]
    return humans
def wall_post():
    con = sqlite3.connect("db/posts.db")
    cur = con.cursor()
    sql = "SELECT * FROM users"
    return cur.execute(sql).fetchall()
def req_friend(id:str, id_to:str, status:str):
    con = sqlite3.connect("db/requests_friends.db")
    cur = con.cursor()
    sql = ''' INSERT INTO req
            VALUES(?,?,?) '''
    if status == "0":
        res = cur.execute("SELECT * FROM req WHERE id=(?)", [id]).fetchall()
        res2 = cur.execute("SELECT * FROM req WHERE id_to=(?)", [id_to]).fetchall()
        cl = 0
        for i in res:
            if i[0] == id and i[1] == id_to:
                cl = 1
        for i in res2:
            if i[0] == id and i[1] == id_to:
                cl = 1
        if cl == 0:
            cur.execute(sql, [id, id_to, status])
            con.commit()
    elif status == "1":
        cur.execute(sql, [id, id_to, status])
        con.commit()
    
def give_friend(id):
    con = sqlite3.connect("db/requests_friends.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM req WHERE id=(?)", [id]).fetchall()
    res2 = cur.execute("SELECT * FROM req WHERE id_to=(?)", [id]).fetchall()
    friends = []
    for i in res:
        if i[2] == "1":
            if i[0] != id:
                friends.append(i[0])
            if i[1] != id:
                friends.append(i[1])
    for i in res2:
        if i[2] == "1":
            if i[0] != id:
                friends.append(i[0])
            if i[1] != id:
                friends.append(i[1])
    return list(dict.fromkeys(friends))

def del_friend(id:str, id_to:str):
    con = sqlite3.connect("db/requests_friends.db")
    cur = con.cursor()
    sql = '''DELETE FROM req WHERE id=(?) and id_to=(?)'''
    cur.execute(sql, [id, id_to])
    con.commit()