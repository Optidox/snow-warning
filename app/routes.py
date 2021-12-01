from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return "Hello, User!"


@app.route('/ph')
def ph():
    return "ph"