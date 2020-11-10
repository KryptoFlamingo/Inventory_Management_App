from models.meal import Meal
from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/manager', methods=['POST', 'GET'])
def manager():
    if flask.request.method == 'POST':
        stock = Meal()
        stock.meal_beef = flask.request.form
        # stock.meal_fish = flask.request.form['fish_meal']
        stock.meal_chicken = flask.request.form
    return render_template('manager.html')


@app.route('/new_table', methods=['POST', 'GET'])
def new_table():
    return render_template('new_table.html')
