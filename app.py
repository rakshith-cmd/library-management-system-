from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# DB Config (use XAMPP's MySQL settings)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='library_db'
)
cursor = conn.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cursor.execute("INSERT INTO books (title, author, status) VALUES (%s, %s, %s)", (title, author, 'Available'))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
