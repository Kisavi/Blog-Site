from . import auth
from flask import render_template


@auth.route('/register')
def signup():
    return render_template('register.html')


@auth.route('/register')
def login():
    return "Login"


@auth.route('/logout')
def logout():
    return "Log out"
