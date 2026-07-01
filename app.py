from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Cloud Business App Running with Database!"

@app.route('/add/<name>')
def add_employee(name):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return f"{name} added to database!"

@app.route('/list')
def list_employees():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    conn.close()
    return str(data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)