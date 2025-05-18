from models.coffee import Coffee
from models.customer import Customer




def main():
    # Create customers
    faith = Customer("Faith")
    john = Customer("John")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Create orders
    faith.create_order(latte, 5.0)
    faith.create_order(latte, 6.0)
    john.create_order(latte, 8.0)
    john.create_order(espresso, 7.0)

    # Test: Orders for latte
    print("Orders for Latte:")
    for order in latte.orders():
        print(f"{order.customer._customer_name} paid {order.price}")

    # Customers who ordered latte
    print("\nCustomers who ordered Latte:")
    for cust in latte.customers():
        print(cust._customer_name)

    # Number of orders
    print(f"\nTotal Latte orders: {latte.num_orders()}")

    # Average price
    print(f"Average price for Latte: {latte.average_price()}")

    # Most aficionado
    top_customer = Customer.most_aficionado(latte)
    if top_customer:
        print(f"Most aficionado for Latte: {top_customer._customer_name}")
    else:
        print("No customers for this coffee yet.")

if __name__ == "__main__":
    main()


