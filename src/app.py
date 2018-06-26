
from flask import Flask, render_template
from src.common.database import Database

__author__ = "jc"

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "APP_SECRET_KEY"


@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def wel():
    return render_template("home.html")

from src.models.users.views import user_blueprint
from src.models.books.views import book_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(book_blueprint, url_prefix="/books")


