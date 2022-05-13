from . import auth


@auth.route('/register')
def signup():
    return "Sign Up"


@auth.route('/register')
def login():
    return "Login"


@auth.route('/logout')
def logout():
    return "Log out"
