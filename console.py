import pdb
from models.meal import Meal
import repositories.meal_repository as meal_repository


meal_repository.delete_all()


meal1 = Meal("beef_meal", id)
meal2 = Meal("chicken_meal", id)
meal3 = Meal("fish_meal", id)


meal_repository.save(meal1)
meal_repository.save(meal2)
meal_repository.save(meal3)


