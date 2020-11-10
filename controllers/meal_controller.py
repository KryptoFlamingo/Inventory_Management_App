from flask import Flask, render_template, request, redirect, Blueprint
from repositories import meal_repository
from models.meal import Meal

meals_blueprint = Blueprint("meals", __name__)


@meals_blueprint.route('/meals')
def all_meals():
    meals = meal_repository.select_all()
    return render_template('meals.html', meals = meals)
