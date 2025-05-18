
class Customer:
    all_customers = []

    def __init__(self, customer_name):
        if not isinstance(customer_name, str) or len(customer_name) < 1 or len(customer_name) > 15:
            raise Exception("name must be a string and characters should be between 1 and 15")

        self._customer_name = customer_name
        Customer.all_customers.append(self)

    def orders(self):
        from .order import Order  
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from .order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from .order import Order
        orders_for_coffee = [order for order in Order.all if order.coffee == coffee]

        if not orders_for_coffee:
            return None

        spending = {}
        for order in orders_for_coffee:
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price

        most_spent_customer = max(spending, key=spending.get)
        return most_spent_customer

    def __repr__(self):
        return f"Customer({self._customer_name})"
