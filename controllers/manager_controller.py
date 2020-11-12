from flask import Flask, render_template, request, redirect, Blueprint
from repositories import meal_repository
from models.meal import Meal
from controllers.meal_controller import *

manager_blueprint = Blueprint("manager", __name__)


# one below puts meals.sql table in memory for page                      OK
### READ
@manager_blueprint.route('/manager', methods=['POST', 'GET'])
def show_meals():
    meals = meal_repository.select_all()
    return render_template('manager.html', meals = meals)


# EDIT
# GET '/manager/<id>/edit'
@manager_blueprint.route("/manager/<id>/edit", methods=['POST', 'GET'])
def edit_meal(id):
    meal = meal_repository.select(id)
    return render_template('/manager/edit.html', meal = meal)


### UPDATE
@manager_blueprint.route("/manager/<id>", methods=['POST'])
def update_meal(id):
    print(request.form)
    name = request.form['name']
    description = request.form['description']
    cost_price = request.form['cost_price']
    selling_price = request.form['selling_price']
    qty_available = request.form['qty_available']
    qty_sold = request.form['qty_sold']
    meal = Meal(name, description, cost_price, selling_price, qty_available, qty_sold, id)
    print(meal)
    meal_repository.update(meal)
    return redirect('/manager')


### NEW
@manager_blueprint.route("/manager/new_meal", methods=['POST', 'GET'])
def new_meal():
    if request.method == 'GET':
        return render_template('/manager/new_meal.html')

    if request.method == 'POST':   
        name = request.form['name']
        description = request.form['description']
        cost_price = request.form['cost_price']
        selling_price = request.form['selling_price']
        qty_available = request.form['qty_available']
        qty_sold = request.form['qty_sold']
        meal = Meal(name, description, cost_price, selling_price, qty_available, qty_sold)
        print(meal)
        meal_repository.save(meal)
        return redirect('/manager')

# # # DELETE                                            
# # DELETE '/meals/<id>'

# delete already exists on the meal_controller, can I just call the function?
@manager_blueprint.route("/manager/<id>/delete", methods=["POST"])
def delete_meal(id):
    manager_repository.delete(id)
    return redirect('/manager')
