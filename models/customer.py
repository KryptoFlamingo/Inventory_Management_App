class Customer:

    def __init__( self, customer_name, meal_order, id = None ):
        self.customer_name = customer_name
        self.meal_order = meal_order
        self.id = id


# need to add a wallet so that people can pay for their order

# the Menu could be passed into the Customer class with all menu 
# items listed as False and when the customer wants a meal they 
# change it to True 