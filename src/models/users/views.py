
from flask import Blueprint, redirect, request, render_template,session,url_for


from src.models.users.user import User
from src.models.users.errors import UserError

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/users/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.login_valid(email, password):
                session['email'] = email
                return redirect(url_for('books.cat'))
        except UserError as e:
                return e.message

    return render_template('users/login.html')


@user_blueprint.route('/users/logout')
def logout():
    session['email']=None
    return redirect(url_for('wel'))


@user_blueprint.route('/users/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for('books.cat'))
        except UserError as e:
            return e.message
    return render_template("users/register.html")

