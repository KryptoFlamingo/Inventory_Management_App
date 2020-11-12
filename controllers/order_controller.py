# from flask import Flask, render_template, request, redirect, Blueprint
# from repositories import order_repository
# from models.order import Order
# from controllers.meal_controller import *
# from controllers.manager_controller import *


# order_blueprint = Blueprint("order", __name__)


# # one below puts to all meals page on nav bar                       OK
# @order_blueprint.route('/meals/new_order')
# def all_meals():
#     meals = meal_repository.select_all()
#     return render_template('meals.html', meals = meals)

# # # NEW
# # # GET '/meals/new_order'
# @meals_blueprint.route("/meals/new_order", methods=['GET'])
# def new_order():
#         meals = meal_repository.select_all()
#         return render_template("meals/new_order.html", all_meals = meals)