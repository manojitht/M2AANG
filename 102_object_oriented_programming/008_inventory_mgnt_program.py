# ### **Problem Title: Inventory Management System**

# **Problem:**
#
# Create a class-based program to manage a store's inventory. The program should use **OOP concepts** such as **inheritance**, **polymorphism**, **encapsulation**, and **abstraction**.

# ### **Requirements:**
#
# 1. **Create a Base Class**:
#    - Class Name: `Item`
#    - Attributes:
#      - `name`: Name of the item.
#      - `price`: Price of the item.
#      - `quantity`: Quantity in stock.
#
#    - Methods:
#      - `add_stock(amount)`: Adds a specified quantity of stock to the item.
#      - `remove_stock(amount)`: Removes a specified quantity of stock if available, otherwise displays a warning.
#      - `display_item()`: Displays the details of the item.
#
# 2. **Create a Derived Class**:
#    - Class Name: `PerishableItem`
#    - Additional Attributes:
#      - `expiry_date`: Expiry date of the item.
#
#    - Overridden Method:
#      - `display_item()`: Displays the item details along with the expiry date.
#
# 3. **Polymorphism**:
#    - Create a method `apply_discount` in the `Item` class that applies a 10% discount to the price.
#    - In the `PerishableItem` class, override `apply_discount` to apply a 20% discount.
#
# 4. **Main Program**:
#    - Create at least one `Item` and one `PerishableItem`.
#    - Perform the following operations:
#      - Add and remove stock for both items.
#      - Apply discounts to both items.
#      - Display the details of both items.
#
# ### **Example Scenario**:
# 1. Create an `Item` named "Laptop" with a price of 1000 and quantity of 10.
# 2. Create a `PerishableItem` named "Milk" with a price of 50, quantity of 20, and expiry date "2025-01-20".
# 3. Add stock of 5 units to both items.
# 4. Remove stock of 3 units from both items.
# 5. Apply discounts to both items and display their updated details.
#
# This problem increases difficulty by introducing **inheritance**, **polymorphism**, and **encapsulation**. When you're ready with your solution, submit it, and I'll evaluate and grade it! 😊


## My Code:
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount
        return self.quantity

    def remove_stock(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print(f"Sorry, available quantity is {self.quantity}, your amount is {amount}.")
        return self.quantity

    def apply_discount(self):
        discount_price = (10 / 100) * self.price
        self.price -= discount_price
        return self.price

    def display_item(self):
        print(f"Item: {self.name}, Rs.{self.price}, No.{self.quantity}")


class PerishableItem(Item):
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date

    def apply_discount(self):
        discount_price = (20 / 100) * self.price
        self.price -= discount_price
        return self.price

    def display_item(self):
        print(f"Perishable Item: {self.name}, Rs.{self.price}, No.{self.quantity}, Exp Date. {self.expiry_date}.")


item = Item("Laptop", 1000, 10)
p_item = PerishableItem("Milk", 50, 20, "2025-01-20")

item.add_stock(5)
p_item.add_stock(5)

item.remove_stock(3)
p_item.remove_stock(3)

item.apply_discount()
p_item.apply_discount()

item.display_item()
p_item.display_item()



## AI Code:
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self._price = price
#         self._quantity = quantity
#
#     def add_stock(self, amount):
#         if amount > 0:
#             self._quantity += amount
#             print(f"Added {amount} units to {self.name}. Total: {self._quantity}.")
#         else:
#             print("Invalid stock amount. Cannot add negative or zero value.")
#         return self._quantity
#
#     def remove_stock(self, amount):
#         if self._quantity >= amount:
#             self._quantity -= amount
#             print(f"Removed {amount} units from {self.name}. Remaining: {self._quantity}.")
#         else:
#             print(f"Insufficient stock of {self.name}. Available: {self._quantity}, Requested: {amount}.")
#         return self._quantity
#
#     def apply_discount(self):
#         discount_price = (10 / 100) * self._price
#         self._price -= discount_price
#         print(f"10% discount applied. New price of {self.name}: Rs.{self._price}.")
#         return self._price
#
#     def display_item(self):
#         print(f"Item: {self.name} | Price: Rs.{self._price} | Quantity: {self._quantity}")
#
#
# class PerishableItem(Item):
#     def __init__(self, name, price, quantity, expiry_date):
#         super().__init__(name, price, quantity)
#         self.expiry_date = expiry_date
#
#     def apply_discount(self):
#         discount_price = (20 / 100) * self._price
#         self._price -= discount_price
#         print(f"20% discount applied. New price of {self.name}: Rs.{self._price}.")
#         return self._price
#
#     def display_item(self):
#         print(
#             f"Perishable Item: {self.name} | Price: Rs.{self._price} | Quantity: {self._quantity} | Expiry Date: {self.expiry_date}")
#
#
# # Testing
# item = Item("Laptop", 1000, 10)
# p_item = PerishableItem("Milk", 50, 20, "2025-01-20")
#
# item.add_stock(5)
# p_item.add_stock(5)
#
# item.remove_stock(3)
# p_item.remove_stock(3)
#
# item.apply_discount()
# p_item.apply_discount()
#
# item.display_item()
# p_item.display_item()











