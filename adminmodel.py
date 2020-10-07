import sqlite3

def check_admin_pw(adminusername):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select adminpassword from admin where adminusername = '{adminusername}' order by primarykey desc;""".format(adminusername = adminusername))

    adminpassword = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return adminpassword


def check_admin():
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select adminusername from admin order by primarykey desc;""")

    db_user = cursor.fetchall()
    admin = []

    for i in range(len(db_user)):
        person = db_user[i][0]
        admin.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return admin


def update(adminusername, adminpassword, fav_color):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""select adminpassword from admin where adminusername = '{adminusername}';""".format(adminusername = adminusername))

    existing_user = cursor.fetchone()

    if existing_user is None:
        return "Incorrect adminusername"
    else:
        cursor.execute("""update admin set adminusername='{adminusername}',adminpassword='{adminpassword}',fav_color='{fav_color}' where adminusername='{adminusername}';""".format(adminusername=adminusername, adminpassword=adminpassword,fav_color=fav_color))
        connection.commit()
        cursor.close()
        connection.close()
        return "Your Details are Updated!"

    return "not Updated!"
