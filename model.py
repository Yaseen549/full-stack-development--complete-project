import sqlite3

def check_pw(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select password from users where username = '{username}' order by primarykey desc;""".format(username = username))

    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password


def check_users():
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select username from users order by primarykey desc;""")

    db_user = cursor.fetchall()
    users = []

    for i in range(len(db_user)):
        person = db_user[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users

def signup(username, password, fav_color):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select password from users where username = '{username}';""".format(username = username))

    existing_user = cursor.fetchone()

    if existing_user is None:
        cursor.execute("""insert into users(username, password, fav_color)values('{username}','{password}','{fav_color}')""".format(username = username, password = password, fav_color = fav_color))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return "User Already Exist!"

    return "Successfully registered!"




def update(username, password, fav_color):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select password from users where username = '{username}';""".format(username = username))

    existing_user = cursor.fetchone()

    if existing_user is None:
        return "Incorrect Username"
    else:
        cursor.execute("""update users set username='{username}',password='{password}',fav_color='{fav_color}' where username='{username}';""".format(username=username, password=password,fav_color=fav_color))
        connection.commit()
        cursor.close()
        connection.close()
        return "Your Details are Updated!"

    return "not Updated!"





def check_admin_pw(adminusername):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select adminpassword from admin where adminusername = '{adminusername}' order by primarykey desc;""".format(adminusername = adminusername))

    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password


def check_admin():
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select adminusername from admin order by primarykey desc;""")

    db_user = cursor.fetchall()
    users = []

    for i in range(len(db_user)):
        person = db_user[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users

# def display_users():
#     connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
#     cursor = connection.cursor()
#     cursor.execute("""select * from users;""")
#
#     all_users = cursor.fetchall()
#
#     connection.commit()
#     cursor.close()
#     connection.close()
#
#     return all_users

def display_users():
    # Edited out actual values
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT primarykey,username,fav_color from users;""")

    data = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return data
