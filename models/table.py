from models.customer import Customer


class Table:

    def __init__(self, table_number, Customers = [], id = None):
      self.table_number = table_number
      self.Customers = Customers
      self.id = id
