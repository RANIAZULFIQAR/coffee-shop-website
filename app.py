from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert into DB
        conn = sqlite3.connect('coffee.db')
        c = conn.cursor()
        c.execute("INSERT INTO contact (name, email, message) VALUES (?, ?, ?)", 
                  (name, email, message))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('contact.html')

# ----- Coffee detail pages -----
@app.route('/espresso')
def espresso():
    return render_template('espresso.html')

@app.route('/latte')
def latte():
    return render_template('latte.html')

@app.route('/cappuccino')
def cappuccino():
    return render_template('cappuccino.html')

# ----- Order Form Submission -----
@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    coffee_type = request.form['coffee_type']
    quantity = request.form['quantity']

    # Insert order into DB
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders (name, coffee_type, quantity) VALUES (?, ?, ?)", 
              (name, coffee_type, quantity))
    conn.commit()
    conn.close()

    return redirect('/menu')

# ----- Optional Admin Page -----
@app.route('/admin')
def admin():
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()

    c.execute("SELECT * FROM contact")
    messages = c.fetchall()

    c.execute("SELECT * FROM orders")
    orders = c.fetchall()

    conn.close()
    return render_template('admin.html', messages=messages, orders=orders)

if __name__ == '__main__':
    app.run(debug=True)