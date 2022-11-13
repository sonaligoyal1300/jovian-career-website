import sqlite3

connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()
command = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""
cursor.execute("Insert into users VALUES('Rishab', '12345')")
connection.commit()
