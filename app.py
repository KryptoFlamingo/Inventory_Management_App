from models.meal import Meal
from flask import Flask, render_template, request, redirect, Blueprint
import flask
from controllers.meal_controller import meals_blueprint
from controllers.manager_controller import manager_blueprint

app = Flask(__name__)

app.register_blueprint(meals_blueprint)
app.register_blueprint(manager_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/new_table', methods=['POST', 'GET'])
# def new_table():
#     return render_template('new_table.html')

