import sqlite3

connection = sqlite3.connect('database.db')


with open('database.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO products (title, price) VALUES (?, ?)",
            ('Keyboard', 120)
            )

cur.execute("INSERT INTO products (title, price) VALUES (?, ?)",
            ('Monitor 4k', 111)
            )

cur.execute("INSERT INTO products (title, price) VALUES (?, ?)",
            ('Aprilia', 111)
            )

# cur.execute("SELECT * FROM products")

# rows = cur.fetchall()

# # Print the data
# for row in rows:
#     print(row)


connection.commit()
connection.close()
