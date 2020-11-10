from db.run_sql import run_sql

from models.meal import Meal

meals = []
# had issue getting meals to be seen, 
# moved out of def so its not a scope issue
# should I be referencing stock from app.py?

def select_all():


    sql = 'SELECT * FROM meals'
    results = run_sql(sql)

#     for dictionary in results:
#         meal = meal_repository.select(dictionary['id'])
#         meal = Meal(dictionary['name'], dictionary['id'])
#         meals.append(meal)
#     return meals
#  copied and editted from books example; dont know how to fix 


def save(meal):
    sql = "INSERT INTO meals (name, id) VALUES (%s, %s) RETURNING * "
    values = [meal.name, meal.id]
    results= run_sql(sql, values)
    # id = results[0]['id']
    # meal.id = id
    # not sure what above means or how to use
    return meal

def delete_all():
    sql = "DELETE FROM meals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM meals WHERE id = %s"
    values = [id]
    run_sql(sql,values)