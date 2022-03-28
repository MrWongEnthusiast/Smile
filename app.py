from flask import Flask, render_template, request, session
import sqlite3
from sqlite3 import Error
DB_NAME = "smile.db"

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

    product_list = [["Flat White","Flat white reminds me of my ex *badoomch* i want you back please text back please","180ml", "flatwhite", "3.00"],
                    ["Chemex","It sounds like something putin would you on populated civilian areas.","200ml","chemex","4.00"],
                    ["Aeropress","Aeropress, just call it a plunger you muppet.","180ml","aeropress","2.00"]]

    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0')
