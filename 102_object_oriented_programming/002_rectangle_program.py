# **Problem:**
# Create a class called `Rectangle` that represents a rectangle shape. The class should have the following attributes:
# - `length`: The length of the rectangle.
# - `width`: The width of the rectangle.
#
# The class should have the following methods:
# 1. A `__init__` method to initialize the `length` and `width`.
# 2. A method called `area` that returns the area of the rectangle (length * width).
# 3. A method called `perimeter` that returns the perimeter of the rectangle (2 * (length + width)).
# 4. A method called `is_square` that returns `True` if the rectangle is a square (i.e., length == width), and `False` otherwise.
#
# Once you've created the class, test it by creating a rectangle and calculating its area, perimeter, and checking if it's a square.
#
# Try this and share your code when you're done!

# My Code:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"The area of the rectangle is {self.length * self.width}")

    def perimeter(self):
        print(f"The perimeter of the rectangle is {2 * (self.length + self.width)}")

    def is_rectangle(self):
        if self.length == self.width:
            return True
        else:
            return False


shape = Rectangle(10, 10)
shape.area()
shape.perimeter()
shape.is_rectangle()

## AI Code:
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         print(f"The area of the rectangle is {self.length * self.width}")
#
#     def perimeter(self):
#         print(f"The perimeter of the rectangle is {2 * (self.length + self.width)}")
#
#     def is_square(self):
#         return self.length == self.width  # Returns True if it's a square, otherwise False
#
#
# shape = Rectangle(10, 10)
# shape.area()
# shape.perimeter()
# print(f"Is this a square? {shape.is_square()}")
