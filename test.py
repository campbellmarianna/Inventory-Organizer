import sqlite3

connection = sqlite3.connect('data.db') # always need a connection \/ and a cursor.

cursor = connection.cursor() # cursor allows you start and stop things - responsible for selecting the queries

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit() # tell it to save to the disc

connection.close() # good practice