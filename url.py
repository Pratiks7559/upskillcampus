from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_url TEXT)''')
    conn.commit()
    conn.close()

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to shorten the URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['original_url']
    short_url = generate_short_url()

    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
    conn.commit()
    conn.close()

    return render_template('shortened.html', short_url=short_url)

# Route to redirect the short URL to the original URL
@app.route('/<short_url>')
def redirect_url(short_url):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM urls WHERE short_url = ?", (short_url,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
