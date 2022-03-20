from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def render_menu_page():

     render_template('menu.html')

app.run(host='0.0.0.0')
