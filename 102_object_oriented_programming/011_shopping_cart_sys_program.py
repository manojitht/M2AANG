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