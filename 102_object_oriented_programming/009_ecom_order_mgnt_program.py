# ### **Problem Title: E-Commerce Order Management System**
# **Problem:**
#
# Build a class-based program to manage an e-commerce platform's order system using **OOP principles**, including **inheritance**, **polymorphism**, **encapsulation**, and **abstraction**.
#
# ### **Requirements:**
#
# 1. **Base Class: `Product`**
#    - Attributes:
#      - `name`: Name of the product.
#      - `price`: Price of the product.
#      - `stock`: Number of items in stock.
#
#    - Methods:
#      - `add_stock(amount)`: Adds stock to the product.
#      - `remove_stock(amount)`: Reduces stock if available; otherwise, display an error message.
#      - `display_product()`: Displays the product details.
#
# 2. **Derived Class: `ElectronicProduct`**
#    - Additional Attributes:
#      - `warranty`: Warranty period of the product in years.
#
#    - Overridden Methods:
#      - `display_product()`: Display product details along with the warranty period.
#
# 3. **Encapsulation:**
#    - Make attributes like `price` and `stock` private, and use getter and setter methods to manipulate them.
#
# 4. **Class: `Order`**
#    - Attributes:
#      - `order_id`: Unique identifier for the order.
#      - `products`: List of products in the order (use composition to link the `Product` class).
#      - `total_amount`: Total price of the order.
#
#    - Methods:
#      - `add_product(product, quantity)`: Adds a product to the order. Deduct the product's stock accordingly. If stock is insufficient, display an error.
#      - `calculate_total()`: Calculates the total amount for the order.
#      - `display_order()`: Displays the order details, including each product and the total amount.
#
# 5. **Main Program:**
#    - Create at least one `Product` and one `ElectronicProduct`.
#    - Create an `Order`, add products to the order, and display the order details.
#    - Handle edge cases, such as insufficient stock, invalid product quantities, or adding products that don’t exist.
#
# ### **Example Scenario:**
#
# 1. Create a `Product` named "T-shirt" with a price of 500 and stock of 50.
# 2. Create an `ElectronicProduct` named "Smartphone" with a price of 20,000, stock of 30, and a 1-year warranty.
# 3. Add 10 units of "T-shirt" and 2 units of "Smartphone" to the order.
# 4. Display the order details, including the total amount and remaining stock of the products.
#
# This problem introduces **composition** (via the `Order` class), in addition to other OOP principles. It's a step up in difficulty and requires more interactions between classes. Submit your solution for grading once you're done! 😊


## My Code:
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, amount):
        if amount > 0:
            self.stock += amount
            print(f"The stock was updated and currently the stock is {self.stock}.")
        else:
            print(f"Sorry! Invalid stock amount entered.")

    def remove_stock(self, amount):
        if 0 < amount <= self.stock:
            self.stock -= amount
            print(f"The stock was removed and currently the stock is {self.stock}.")
        else:
            print(f"Sorry! Invalid stock amount entered.")

    def display_product(self):
        product_name = self.name
        product_price = self.price
        product_stock = self.stock
        print(f"Product: {product_name}, Price: {product_price}, Stock: {product_stock}.")


class ElectronicProduct(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.warranty = warranty

    def display_product(self):
        product_name = self.name
        product_price = self.price
        product_stock = self.stock
        product_warranty = self.warranty
        print(
            f"Product: {product_name}, Price: {product_price}, Stock: {product_stock}, Warranty: {product_warranty} years.")


# class Order:
#     def __init__(self, order_id, total_amount):
#         self.order_id = order_id
#         self.product = Product(name, price, stock)
#         self.products = []
#         self.total_amount = totaL_amount
#
#     def add_product(self, product, quantity):
#         if product == self.product.name and
            ## continue from here.









