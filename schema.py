import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)

cursor = connection.cursor()

cursor.execute(

    """CREATE TABLE users(primarykey INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(20),password VARCHAR(20),fav_color VARCHAR(20));"""

)

connection.commit()
cursor.close()
connection.close()
