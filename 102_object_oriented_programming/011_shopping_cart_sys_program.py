# ### **OOP Practice Problem: E-Commerce Shopping Cart System**
# **Difficulty Rating:** 8/10 (Advanced)
#
# ---
#
# ### **Problem Statement:**
# Design an **E-Commerce Shopping Cart System** where users can browse, add, and purchase products. The system should support different types of products and provide functionality to manage the cart, apply discounts, and process orders.
#
# ---
#
# ### **Requirements:**
#
# #### **1. Product Management:**
# - Create a base class `Product` with attributes:
#   - `product_id` (Unique ID for each product)
#   - `name`
#   - `price`
#   - `quantity_in_stock`
# - Include methods to:
#   - Display product details.
#   - Check product availability.
#
# - Create two subclasses:
#   - **Electronics**: Add attributes like `brand` and `warranty` (in years).
#   - **Clothing**: Add attributes like `size` and `material`.
#
# ---
#
# #### **2. Shopping Cart:**
# - Create a `ShoppingCart` class with:
#   - A dictionary or list to store products and their quantities.
#   - Methods to:
#     - Add a product to the cart (check availability).
#     - Remove a product from the cart.
#     - View all items in the cart.
#     - Calculate the total price of items in the cart.
#     - Apply a **10% discount** if the total price exceeds a threshold (e.g., $500).
#
# ---
#
# #### **3. Order Processing:**
# - Create an `Order` class to:
#   - Store cart items, total price, and an order ID.
#   - Process the order by:
#     - Deducting the purchased quantities from the stock.
#     - Generating a receipt with order details.
#
# ---
#
# #### **4. Display and Interaction:**
# - Allow users to:
#   - View available products.
#   - Add/remove items to/from the shopping cart.
#   - View cart details and checkout.
#
# ---
#
# ### **Functionalities to Implement:**
# 1. Add multiple types of products to the system.
# 2. Add/remove products to/from the cart.
# 3. Validate product availability before adding to the cart.
# 4. Checkout and process the order with discount eligibility.
# 5. Display a detailed receipt for the order.
#
# ---
#
# ### **Example Interaction:**
#
# 1. Add Products:
#    - `Electronics`: Laptop (Brand: Dell, Warranty: 2 years)
#    - `Clothing`: T-Shirt (Size: M, Material: Cotton)
#
# 2. Add to Cart:
#    - Add 2 Laptops and 5 T-Shirts to the cart.
#
# 3. View Cart:
#    - Show details of all items in the cart with the total price.
#
# 4. Apply Discount:
#    - If total price > $500, apply 10% discount.
#
# 5. Checkout:
#    - Deduct quantities from stock and display an order receipt.
#
# ---
#
# ### **Constraints:**
# - Ensure proper validation (e.g., no negative quantities, stock limits).
# - Encapsulate logic in appropriate classes and methods.

# Let me know when you're done or if you have questions while solving! 😊

## My Code
class Product:
    def __init__(self, product_id: int, name: str, price: float, quantity_in_stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def check_availability(self, name):
        if self.quantity_in_stock > 0:
            print(f"The product {name} is available.")
            return True
        else:
            print(f"Sorry product {name} not available.")
            return False

    def display_products(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"No.of.items: {self.price}")

class Electronic(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity_in_stock: int, brand: str, warranty: float):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.brand = brand
        self.warranty = warranty

    def check_availability(self, name):
        super().check_availability(name)

    def display_products(self):
        super().display_products()
        print(f"Product Brand: {self.brand}")
        print(f"Product Warranty: {self.warranty} Yrs")

class Clothing(Product):
    def __init__(self, product_id: int, name: str, price: float, quantity_in_stock: int, size: str, material: str):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def check_availability(self, name):
        super().check_availability(name)

    def display_products(self):
        super().display_products()
        print(f"Product Size: {self.size}")
        print(f"Product Material: {self.material}")

class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.check_availability(product.name):
            self.products[product.name] = [product, quantity, quantity * product.price]
            print(f"Product {product.name} with quantity {quantity} added to the cart!")
        else:
            print(f"Product {product.name} not available with quantity of {quantity}!")

    def remove_product(self, product):
        if product.name in self.products.keys():
            self.products.pop(product.name)
            print(f"Successfully removed product {product.name} from cart.")
        else:
            print(f"No product {product.name} found in cart.")

    def view_items(self):
        print("__________________________________________________")
        print("                 Cart Items List                  ")
        print("__________________________________________________")
        count = 0
        for product, quantity in self.products.items():
            count += 1
            print(f"Product: {product}  ->  Quantity: {quantity[1]}  ->  Price: ${quantity[2]}")
        print("__________________________________________________")
        print(f"           Total cart items: {count}             ")
        print("__________________________________________________")

    def apply_discount(self, price):
        if price > 500:
            discount = (10 / 100) * price
            new_price = price - discount
            print(f"Eligible for discount of 10% and the discounted price is ${new_price}")
            return new_price
        else:
            print(f"Not eligible for discount!")
            return price

    def calculate_price(self):
        total_price = 0
        for price in self.products.values():
            total_price += price[2]
        print(f"Total price of the cart items is ${self.apply_discount(total_price)}.")


class Order:
    def __init__(self, order_id: int, total_price: float, shopping_cart):
        self.order_id = order_id
        self.total_price = total_price
        self.shopping_cart = shopping_cart

    def process_order(self):
        for product in self.shopping_cart.values():
            product_obj = product[0]
            deduct_quantity = product[1]
            remaining_quantity = product_obj.quantity_in_stock - deduct_quantity
            product_obj.quantity_in_stock = remaining_quantity

        print("__________________________________________________")
        print(f"            Order Receipt: {self.order_id}       ")
        print(self.shopping_cart.view_items())
        print("__________________________________________________")
        print(self.shopping_cart.calculate_price())
        print("__________________________________________________")


laptop = Electronic(100, "Aspiron Laptop", 900, 10, "Dell", 2)
tshirt = Clothing(101, "Abbrow T-Shirt", 50, 25, "M", "Lenin")
categories = [laptop, tshirt]

print("""
------------------------------------------------------
        Welcome to our World One Online store!
------------------------------------------------------
                  Menu option list
------------------------------------------------------
Press 1: to view the available products.
Press 2: to add the items on the cart.
Press 3: to remove items from the cart.
Press 4: to view cart details.
Press 5: to checkout and process the order receipt.
-----------------------------------------------------
""")

command = str(input("Enter 'Yes' to shopping (or) Enter 'Exit' to close: ")).lower()
while command != "exit":
    option = int(input("Enter your option: "))
    if option == 1:
        count = 0
        for category in categories:
            count += 1
            print(f"Product No. {count}:")
            category.display_products()
            print("\n")
    elif option == 2:
        item_name = int(input("Enter the product number: "))
        quantity = int(input(f"Enter quantity of product number {item_name}: "))
        product = categories[item_name - 1]
        cart = ShoppingCart()
        cart.add_product(product, quantity)
    # elif option == 3:





















