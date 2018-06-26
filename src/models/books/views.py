import sys

import PyPDF2
sys.path.insert(0,'F:\\books')
from flask import Blueprint, render_template, redirect, url_for, request, session
import src.models.books.error as errors
from src.common.database import Database
Database.initialize()
from src.models.collection.category import category
from src.models.books.book import Book

book_blueprint=Blueprint('books',__name__)


@book_blueprint.route('/<string:id>',methods=['GET','POST'])
def book(id):
    if request.method=='POST':

        if(Database.find_one('favourite',{'_id':id}) is None):
            Book.savfav(id)
            return redirect(url_for('.fav'))
        else:
            raise errors.AlreadyExistsError("Already Added to favourite list")

    book=Book.find_by_id(id)
    return render_template('books/book.html',book=book)
@book_blueprint.route('/collection/<string:id>')
def home(id):

    books=Book.by_category_id(id)
    return render_template('books/books.html',books=books)
@book_blueprint.route('/fav')
def fav():
    favs=Book.query()
    return render_template('books/fav.html', favs=favs)

@book_blueprint.route('/books/new',methods=['GET','POST'])
def add():
    if request.method=='POST':
        author=request.form['author']
        title=request.form['title']
        year=request.form['year']
        description=request.form['description']
        link=request.form['link']
        cs=request.form['category']
        b=category.by_name(cs)
        if b is None:
            b=category(cs)
            b.save()

        book=Book(author=author,category_id=b._id,title=title,link=link,description=description,year=year)
        book.save()


    return render_template('books/new.html')
@book_blueprint.route('/books/update/<string:id>',methods=['POST','GET'])
def update(id):
    if request.method=='POST':
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']
        updated_time = request.form['updated_time']
        link=request.form['link']
        book = Book.find_by_id(id)
        book.author=author
        book.title=title
        book.year=year
        book.updated_time=updated_time
        book.description=description
        book.link=link
        book.save()
    return render_template('books/update.html',book=Book.find_by_id(id))
@book_blueprint.route('/categories')
def cat():
    categories=category.query()
    return render_template('collection/all.html',categories=categories)

@book_blueprint.route('/view/<string:id>/<int:number>')
def view(id,number):

    link=Book.find_by_id(id).link

    pdfFileObj = open('F:/books/'+link+'.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(number)
    text=pageObj.extractText()
    return render_template('books/pdfread.html',text=text,id=id,number=number)

