class Order:
    def __init__(self, id= None, order_number, order_raised, meals_id, order_qty):
        self.id = id
        self.order_number = order_number
        self.order_raised = order_raised
        meals_id = meals_id
        order_qty = order_qty


# below is the SQL which relates to the class above
# CREATE TABLE orders (
#   id SERIAL PRIMARY KEY,
#   order_number INT,
#   order_raised datetime DEFAULT CURRENT_TIMESTAMP,
#   meals_id INT REFERENCES meals(id),
#   order_qty INT