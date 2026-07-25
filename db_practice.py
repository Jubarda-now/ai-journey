import sqlite3

connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor_name TEXT,
        message TEXT
    )
""")

cursor.execute("INSERT INTO messages (visitor_name, message) VALUES (?, ?)", ("Brady", "This is my first saved message!"))
connection.commit()

cursor.execute("SELECT * FROM messages")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()