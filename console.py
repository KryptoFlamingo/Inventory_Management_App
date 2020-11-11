import pdb
from models.meal import Meal
import repositories.meal_repository as meal_repository


meal_repository.delete_all()


meal1 = Meal("beef_meal", "Beef Meal", 5, 6, 2, 0)
meal2 = Meal("chicken_meal", "Chicken Meal", 5, 6, 0, 0)
meal3 = Meal("fish_meal", "Fish Meal", 7, 8, 5, 0)



meal_repository.save(meal1)
meal_repository.save(meal2)
meal_repository.save(meal3)


