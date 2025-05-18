
       
class Coffee:
    def __init__(self, coffee_name):
        if not isinstance(coffee_name, str) or len(coffee_name) <= 3:
            raise Exception("name must be a string and with more than 3 characters")
        self._coffee_name = coffee_name

    def orders(self):
        from .order import Order  
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)




