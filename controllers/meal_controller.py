from flask import Flask, render_template, request, redirect, Blueprint
from repositories import meal_repository
from models.meal import Meal

meals_blueprint = Blueprint("meals", __name__)


@meals_blueprint.route('/meals')
def all_meals():
    meals = meal_repository.select_all()
    return render_template('meals.html', meals = meals)

@meals_blueprint.route("/meals/<id>/delete", methods=["POST"])
def delete_meal(id):
    meal_repository.delete(id)
    return redirect('/meals')

# @books_blueprint.route("/books/new")
# def new_book():
#     authors = author_repository.select_all()
#     return render_template("books/new.html", authors = authors)

# @books_blueprint.route("/books", methods=['POST'])
# def add_book():
#     title = request.form['title']
#     genre = request.form['genre']
#     author_id   = request.form['author_id']
#     author = author_repository.select(author_id)
#     new_book = Book(title, genre, author)
#     book_repository.save(new_book)
#     return redirect('/books')

# @books_blueprint.route("/books/<id>/edit")
# def edit_book(id):
#     book = book_repository.select(id)
#     authors = author_repository.select_all()
#     return render_template('books/edit.html', book = book, authors = authors)

# @books_blueprint.route("/books/<id>", methods=['POST'])
# def update_book(id):
#     title = request.form['title']
#     genre = request.form['genre']
#     author_id   = request.form['author_id']
#     author = author_repository.select(author_id)
#     book = Book(title, genre, author, id)
#     book_repository.update(book)
#     return redirect('/books')


