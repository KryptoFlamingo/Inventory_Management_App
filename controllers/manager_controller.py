from flask import Flask, render_template, request, redirect, Blueprint
from repositories import meal_repository
from models.meal import Meal
from controllers.meal_controller import *

manager_blueprint = Blueprint("manager", __name__)


# one below puts meals.sql table in memory for page                      OK
@manager_blueprint.route('/manager', methods=['POST', 'GET'])
def manager():
    meals = meal_repository.select_all()
    return render_template('manager.html')


# READ
@manager_blueprint.route("/manager", methods=['GET'])
def show_meals():
    meals = meal_repository.select()
    return render_template('manager.html')

# # # EDIT
# # # GET '/books/<id>/edit'
# # @books_blueprint.route("/books/<id>/edit", methods=['GET'])
# # def edit_book(id):
# #     book = book_repository.select(id)
# #     authors = author_repository.select_all()
# #     return render_template('books/edit.html', book = book, all_authors = authors)

# # # UPDATE
# # # PUT '/books/<id>'
# # @books_blueprint.route("/books/<id>", methods=['POST'])
# # def update_book(id):
# #     title    = request.form['title']
# #     genre = request.form['genre']
# #     publisher   = request.form['publisher']
# #     author  = author_repository.select(request.form['author_id'])
# #     book = Book(title, genre, publisher, author, id)
# #     print(book.author.full_name())
# #     book_repository.update(book)
# #     return redirect('/books')



# # # DELETE                                            
# # DELETE '/meals/<id>'

# delete already exists on the meal_controller, can I just call the function?
# @manager_blueprint.route("/manager/<id>/delete", methods=["POST"])
# def delete_meal(id):
#     manager_repository.delete(id)
#     return redirect('/manager')
