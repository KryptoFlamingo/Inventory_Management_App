class Meal:
    def __init__(self, name, description, cost_price, selling_price, qty_available, qty_sold, id = None):
        self.name = name
        self.description = description
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.qty_available = qty_available
        self.qty_sold = qty_sold
        self.id = id

# need to add a meal cost to link with the user wallet and pay for 
# food - will add later once the rest is sorted