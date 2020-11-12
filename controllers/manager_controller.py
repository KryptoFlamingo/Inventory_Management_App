from flask import Flask, render_template, request, redirect, Blueprint
from psycopg2.extras import DictConnection
from repositories import meal_repository
from models.meal import Meal
from controllers.meal_controller import *

manager_blueprint = Blueprint("manager", __name__)


# one below puts meals.sql table in memory for page                      OK
### READ
@manager_blueprint.route('/manager', methods=['POST', 'GET'])
def show_meals():
    meals = meal_repository.select_all()
    data = financials(meals)
    print(data)
    return render_template('manager.html', meals = meals, data = data)


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




### FUNCTIONS TO CALCULATE FINANCIAL METRICS BASED ON MEALS SQL TABLE CONTENT
def financials(meals):
    list = []
    data = {}
    running_total = 0

    for meal in meals:
# FORECASTS
# TOTAL FORECAST SALES/
        full_stock_qty = meal.qty_available + meal.qty_sold
        total_forecast_sales = meal.selling_price * full_stock_qty
        # running_total = running_total + total_forecast_sales_for_meal

# TOTAL FORECAST PROFIT/
        total_forecast_profit = total_forecast_sales - (meal.cost_price * full_stock_qty)
        # running_total = running_total + total_forecast_profit

        data = {
            'meal_id' : meal.id,
            'total_forecast_sales' : total_forecast_sales,
            'total_forecast_profit' : total_forecast_profit
        }
        list.append(data)
    return list

# # ACTUALS
#         total_actual_sales = meal.selling_price * meal.qty_sold
#         data[meal.id].append(total_actual_sales)
#         profit_per_meal = meal.selling_price - meal.cost_price
#         data[meal.id].append(profit_per_meal)
#         total_actual_profit = profit_per_meal * meal.qty_sold
#         data[meal.id].append(total_actual_profit)
    data["total_forecast_sales"] = running_total
    data["total_forecast_sales"] = running_total
    return data


