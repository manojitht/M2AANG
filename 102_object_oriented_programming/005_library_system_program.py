# **Problem: Library System**
#
# Create a class `Library` to manage a collection of books. The class should have the following features:
#
# 1. **Attributes**:
#    - `books`: A dictionary where the keys are book titles and the values are the number of copies available.
#
# 2. **Methods**:
#    - `add_book(title, copies)`: Adds a specific number of copies of a book to the library.
#    - `lend_book(title)`: Allows a user to borrow a book. This decreases the number of available copies by 1. If the book is unavailable, print a message saying so.
#    - `return_book(title)`: Allows a user to return a book. This increases the number of available copies by 1.
#    - `display_books()`: Displays all the books in the library with the number of available copies.
#
# ---
#
# **Example Scenario:**
# 1. Add two books ("The Alchemist" with 3 copies, and "1984" with 5 copies).
# 2. Lend a copy of "The Alchemist".
# 3. Display the books after lending.
# 4. Return the borrowed book.
# 5. Display the books again.
#
# ---
#
# Take your time, and when you're ready, submit your solution for grading! 😊


## My Code:
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies):
        self.books[title] = copies
        print(f"The {title} with copies of {copies} was added to the library!")

    def lend_book(self, title):
        if title in self.books.keys():
            copies = self.books[title] - 1
            self.books[title] = copies
            print(f"The {title} was lended from the library available copies {self.books[title]}")
        else:
            print(f"The {title} of book is unavailable in the library!")

    def return_book(self, title):
        if title in self.books.keys():
            copies = self.books[title] + 1
            self.books[title] = copies
            print(f"The {title} was returned to the library, available copies {self.books[title]}")
        else:
            print(f"The {title} of book is unavailable in the library!")

    def display_books(self):
        for book in self.books.keys():
            print(f"Title: {book} has {self.books[book]} copies.")


library = Library()
library.add_book("The Alchemist", 3)
library.add_book("1984", 5)
library.lend_book("The Alchemist")
library.display_books()
library.return_book("The Alchemist")
library.display_books()


## AI Code:
# class Library:
#     def __init__(self):
#         self.books = {}
#
#     def add_book(self, title, copies):
#         if title in self.books:
#             self.books[title] += copies
#             print(f"{copies} more copies of '{title}' were added to the library!")
#         else:
#             self.books[title] = copies
#             print(f"'{title}' with {copies} copies was added to the library!")
#
#     def lend_book(self, title):
#         if title in self.books:
#             if self.books[title] > 0:
#                 self.books[title] -= 1
#                 print(f"'{title}' was lent out. Remaining copies: {self.books[title]}")
#             else:
#                 print(f"'{title}' is currently out of stock!")
#         else:
#             print(f"'{title}' is unavailable in the library!")
#
#     def return_book(self, title):
#         if title in self.books:
#             self.books[title] += 1
#             print(f"'{title}' was returned to the library. Available copies: {self.books[title]}")
#         else:
#             print(f"'{title}' does not belong to this library. Cannot return!")
#
#     def display_books(self):
#         if self.books:
#             print("Books available in the library:")
#             for book, copies in self.books.items():
#                 print(f"  - {book}: {copies} copies")
#         else:
#             print("The library is currently empty.")
#
#
# # Test the updated class
# library = Library()
# library.add_book("The Alchemist", 3)
# library.add_book("1984", 5)
# library.lend_book("The Alchemist")
# library.display_books()
# library.lend_book("The Alchemist")
# library.lend_book("The Alchemist")
# library.lend_book("The Alchemist")  # Out of stock
# library.return_book("The Alchemist")
# library.display_books()


## Suggestions for Improvement:

# Validation for Lending Books:
#
# Currently, the code does not check if a book has zero copies before lending. It allows the number of copies to become negative. You should add a condition to prevent lending when there are no copies left.
# Validation for Adding Books:
#
# If the book already exists in the library, instead of overwriting the existing number of copies, consider adding to the existing count.
# Code Simplification:
#
# The dictionary's keys() method is not needed when checking for a key's existence. Using title in self.books is sufficient and more Pythonic.
