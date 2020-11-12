from flask import Flask, render_template, request, redirect, Blueprint
from repositories import meal_repository
from models.meal import Meal

meals_blueprint = Blueprint("meals", __name__)


# one below puts to all meals page on nav bar                       OK
@meals_blueprint.route('/meals')
def all_meals():
    meals = meal_repository.select_all()
    return render_template('meals.html', meals = meals)


# # NEW
# # GET '/meals/new_order'
# to action the order button and reduce qty_available by 1 per submit action
@meals_blueprint.route("/meals/<id>/order", methods=['GET', 'POST'])
def new_order(id):
        order = meal_repository.select(id)
        order.qty_available = order.qty_available - 1
        order.qty_sold = order.qty_sold + 1
        meal_repository.update(order)
        return redirect ('/meals')





# # CREATE
# # POST '/meals'
@meals_blueprint.route("/meals", methods=['POST'])
def create_order():
    name = "order" 
    value = "{{ meal.id }}"
    {{ meal.description }}
    name = "qty" 
    type = "number"
    order = Meal()
    meal_repository.save(Meal)
    return redirect ('/meals')
# @books_blueprint.route("/books",  methods=['POST'])
# def create_book():
#     title    = request.form['title']
#     genre = request.form['genre']
#     publisher   = request.form['publisher']
#     author  = author_repository.select(request.form['author_id'])
#     book = Book(title, genre, publisher, author)
#     book_repository.save(book)
#     return redirect('/books')

# @meals_blueprint.route("/order", methods=["POST"])
# def new_order():
#     qty = flask.request.form["qty"]
#     meal_id = flask.request.form["id"]
#     description = flask.request.form["description"]
#     # meals = meal_repository.select_all()
#     # return render_template("meals.html", meals = meals)
#     new_order = Meal()
#     # if it currently gets an order from the meal page of a qty of meals how does it give it back? 
#     task_repository.save(new_order)
#     return redirect('/order')
#     # dont know what the above actually means or does




# # SHOW
# # GET '/books/<id>'
# @books_blueprint.route("/books/<id>", methods=['GET'])
# def show_book(id):
#     book = book_repository.select(id)
#     return render_template('books/show.html', book = book)

# # EDIT
# # GET '/books/<id>/edit'
# @books_blueprint.route("/books/<id>/edit", methods=['GET'])
# def edit_book(id):
#     book = book_repository.select(id)
#     authors = author_repository.select_all()
#     return render_template('books/edit.html', book = book, all_authors = authors)

# # UPDATE
# # PUT '/books/<id>'
# @books_blueprint.route("/books/<id>", methods=['POST'])
# def update_book(id):
#     title    = request.form['title']
#     genre = request.form['genre']
#     publisher   = request.form['publisher']
#     author  = author_repository.select(request.form['author_id'])
#     book = Book(title, genre, publisher, author, id)
#     print(book.author.full_name())
#     book_repository.update(book)
#     return redirect('/books')

# # DELETE                                            OK
# # DELETE '/books/<id>'
@meals_blueprint.route("/meals/<id>/delete", methods=["POST"])
def delete_meal(id):
    meal_repository.delete(id)
    return redirect('/meals')
