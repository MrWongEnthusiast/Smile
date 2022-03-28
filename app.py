from flask import Flask, render_template, request, session
import sqlite3
from sqlite3 import Error

DB_NAME = "USC.db"

app = Flask(__name__)


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)


@app.route('/')
def render_home_page():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    con = create_connection(DB_NAME)

    query = "SELECT name, description, volume, price, image FROM product"

    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    con.close()

    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0')

# http://10.50.16.37:5000/
