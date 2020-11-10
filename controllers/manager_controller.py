from flask import Flask, render_template, request, redirect, Blueprint
from repositories import meal_repository
from models.meal import Meal

manager_blueprint = Blueprint("manager", __name__)


# @meals_blueprint.route('/manager')
# def all_meals():
#     meals = meal_repository.select_all()
#     return render_template('meals.html', meals = meals)

@manager_blueprint.route('/manager', methods=['POST', 'GET'])
def manager():
#     if flask.request.method == 'POST':
#         stock = Meal()
#         stock.meal_beef = flask.request.form
#         # stock.meal_fish = flask.request.form['fish_meal']
#         stock.meal_chicken = flask.request.form
    return render_template('manager.html')
