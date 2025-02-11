# coding: utf-8

import sqlite3

conn = sqlite3.connect('my_Db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS pWdB(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTEGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("jeanne", 30))
conn.commit()

cursor.execute("""SELECT name, age FROM users""")
user1 = cursor.fetchone()
print(user1)

conn.close()