from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect("messages.db")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visitor_name TEXT,
            message TEXT
        )
    """)
    return connection

@app.route("/")
def home():
    return "<h1>Welcome to my site!</h1><p><a href='/about'>About</a> | <a href='/contact'>Contact</a> | <a href='/messages'>View Messages</a></p>"

@app.route("/about")
def about():
    return "<h1>About Me</h1><p>I'm Brady, and I'm learning to build apps with Python and LLMs.</p><p><a href='/'>Back home</a></p>"

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return """
    <h1>Contact</h1>
    <form action="/submit" method="POST">
        <label>Your name: <input type="text" name="visitor_name"></label><br><br>
        <label>Your message: <input type="text" name="message"></label><br><br>
        <button type="submit">Send</button>
    </form>
    <p><a href='/'>Back home</a></p>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("visitor_name")
    message = request.form.get("message")

    connection = get_db_connection()
    connection.execute("INSERT INTO messages (visitor_name, message) VALUES (?, ?)", (name, message))
    connection.commit()
    connection.close()

    return f"<h1>Thanks, {name}!</h1><p>Your message was saved.</p><p><a href='/'>Back home</a></p>"

@app.route("/messages")
def view_messages():
    connection = get_db_connection()
    rows = connection.execute("SELECT * FROM messages").fetchall()
    connection.close()

    html = "<h1>All Messages</h1><ul>"
    for row in rows:
        html += f"<li>{row[1]} said: {row[2]}</li>"
    html += "</ul><p><a href='/'>Back home</a></p>"
    return html

if __name__ == "__main__":
    app.run(debug=True)