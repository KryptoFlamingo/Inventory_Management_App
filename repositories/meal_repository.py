from db.run_sql import run_sql

from models.meal import Meal


# had issue getting meals to be seen, 
# moved out of def so its not a scope issue
# should I be referencing stock from app.py?

def select_all():

    sql = 'SELECT * FROM meals'
    results = run_sql(sql)
    meals = []
    for dictionary in results:
        meal = Meal(dictionary['name'], dictionary['description'], dictionary['cost_price'], dictionary['selling_price'], dictionary['qty_available'], dictionary['qty_sold'], dictionary['id'])
        meals.append(meal)
    return meals
#  copied and editted from books example; dont know how to fix 

def save(meal):
    sql = "INSERT INTO meals (name, description, cost_price, selling_price, qty_available, qty_sold) VALUES (%s, %s, %s, %s, %s, %s) RETURNING * "
    values = [meal.name, meal.description, meal.cost_price, meal.selling_price, meal.qty_available, meal.qty_sold]
    results= run_sql(sql, values)
    id = results[0]['id']
    meal.id = id
    return meal

def delete_all():
    sql = "DELETE FROM meals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM meals WHERE id = %s"
    values = [id]
    run_sql(sql,values)