from . import auth
from flask import render_template, request, flash


@auth.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Pick a username that is greater than 2 characters.', category='error')
        elif len(password1) < 7:
            flash('Use a stronger password that is more than 7 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords did not match!!!', category='error')
        else:
            # create a new user if form is valid
            flash('Account created successfully.', category='success')

    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('register.html')


@auth.route('/logout')
def logout():
    return "Log out"
