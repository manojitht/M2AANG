# **Problem:**
# Create a class called `Book` that represents a book in a library. The class should have the following attributes:
# - `title`: The title of the book.
# - `author`: The author of the book.
# - `year`: The year the book was published.
# - `is_borrowed`: A boolean attribute to track whether the book is borrowed (True if borrowed, False otherwise).
#
# The class should have the following methods:
# 1. A `__init__` method to initialize the book's attributes.
# 2. A method called `borrow` that sets `is_borrowed` to `True`.
# 3. A method called `return_book` that sets `is_borrowed` to `False`.
# 4. A method called `display_info` that displays the book's details (title, author, year, and borrow status).
#
# Once you've created the class, test it by creating a book, borrowing it, returning it, and displaying its information.

## My Code:
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrowed_book(self):
        self.is_borrowed = True

    def returned_book(self):
        self.is_borrowed = False

    def details(self):
        print(f"{self.title}, {self.author}, {self.year}, {self.is_borrowed}.")


Fire = Book("Wings of Fire", "A.P.J Abdul Kalam", "2010")
Fire.borrowed_book()
Fire.details()
Fire.returned_book()
Fire.details()


## AI Code:
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.is_borrowed = False
#
#     def borrow(self):
#         self.is_borrowed = True
#
#     def return_book(self):
#         self.is_borrowed = False
#
#     def display_info(self):
#         borrow_status = "Borrowed" if self.is_borrowed else "Not Borrowed"
#         print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {borrow_status}")
#
#
# book = Book("Wings of Fire", "A.P.J Abdul Kalam", "2010")
# book.borrow()
# book.display_info()
# book.return_book()
# book.display_info()
