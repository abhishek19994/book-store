from functools import wraps

from flask import session, redirect, url_for, request

from src.app import app


def requires_login(func):
    @wraps(func)
    def decorated_function(*args,**kwargs):
        if 'email' not in session.keys() or  session['email'] is None:
            return redirect(url_for('users.login',next=request.path))
        return func(*args,**kwargs)
    return decorated_function
def requires_admin_permission(func):
    @wraps(func)
    def decorated_function(*args,**kwargs):
        if 'email' not in session.keys() or  session['email'] is None:
            return redirect(url_for('users.login',next=request.path))
        if session['email'] not in app.config['ADMINS']:
            return redirect(url_for('users.login'))
        return func(*args,**kwargs)
    return decorated_function