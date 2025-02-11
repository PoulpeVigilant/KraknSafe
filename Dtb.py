# coding: utf-8

import sqlite3

def CreatedB():
     conn = sqlite3.connect('my_Db')
     cursor = conn.cursor()
     cursor.execute("""
     CREATE TABLE IF NOT EXISTS dB(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     userID TEXT,
     pw TEXT
     )
     """)
     conn.commit()
     conn.close()
     return()

#CreateTable()

def FilldB(name,userID,pw):
     conn = sqlite3.connect('my_Db')
     cursor = conn.cursor()
     cursor.execute("""
     INSERT INTO dB(name, userID, pw) VALUES(?, ?, ?)""", (name, userID,pw))
     conn.commit()
     conn.close()
     return()

#FilldB("jean","yolo33","gyu8M")
#FilldB("Manon","Héli","33")

def DeletedB():
     conn = sqlite3.connect('my_Db')
     cursor = conn.cursor()
     cursor.execute("""DELETE FROM dB WHERE id = 1""")
     conn.commit()
     conn.close()
     return()


#DeletedB()

def UpdatedB():
     conn = sqlite3.connect('my_Db')
     cursor = conn.cursor()
     cursor.execute("""UPDATE dB SET name = "yo31" WHERE id = 2""")
     conn.commit()
     conn.close()
     return()

#UpdatedB()

def DeleteTable():
     conn = sqlite3.connect('my_Db')
     cursor = conn.cursor()
     cursor.execute("""
     DROP TABLE pWdB
""")
     conn.commit()
     conn.close()
     return()

#DeleteTable()

def FetchDB():
     conn = sqlite3.connect('my_Db')
     cursor = conn.cursor()
     cursor.execute("""SELECT name FROM dB""")
     user = cursor.fetchone()
     print(user)
     conn.close()
     return()

#FetchDB()