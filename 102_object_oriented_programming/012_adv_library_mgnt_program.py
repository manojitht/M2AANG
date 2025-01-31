# Got it! I'll ensure that all future questions are advanced-level, challenging your OOP, algorithmic, and Python skills to the fullest. Here's your next advanced-level question:
#
# **Advanced Question (Difficulty: 🔥🔥🔥🔥🔥)**
# **Build an Advanced Library Management System**
#
# Design and implement an advanced library management system using Python. This system should support the following features:
#
# ### **Requirements:**
# 1. **Entities and Relationships:**
#    - **Books:** Each book has attributes such as `book_id`, `title`, `author`, `genre`, `quantity`, and `publication_year`.
#    - **Members:** Each member has `member_id`, `name`, `email`, and a list of books they have borrowed.
#    - **Librarians:** A librarian can add/remove books and oversee member operations.
#
# 2. **Features:**
#    - **Search:** Members can search for books by title, author, genre, or publication year. The search results should allow for sorting by any attribute (e.g., by title, author).
#    - **Borrow/Return:** Members can borrow books (up to 5 at a time) and return them. Update the book's quantity accordingly.
#    - **Overdue Tracking:** Track when a member borrows a book and calculate overdue fees if the book isn’t returned within 14 days. Fee: `$0.50/day` after the due date.
#    - **Notifications:** Send reminders (print/log messages) to members for overdue books.
#    - **Membership Management:** Librarians can add/remove members.
#
# 3. **Data Structures and Algorithms:**
#    - Use appropriate **Python data structures** to handle book storage, searching, and member data efficiently.
#    - Implement **sorting algorithms** for displaying search results.
#
# 4. **Advanced OOP Concepts:**
#    - Utilize **inheritance**, **polymorphism**, **encapsulation**, and **abstraction** effectively.
#    - Implement `@staticmethod` and `@classmethod` where appropriate.
#    - Use **custom exceptions** to handle cases such as:
#      - Borrowing more than 5 books.
#      - Returning a book not borrowed.
#      - Searching for a book that doesn’t exist.
#
# 5. **Additional Features:**
#    - Generate detailed **transaction receipts** for book borrow/return actions.
#    - Generate **member activity reports** summarizing borrowed books, overdue fees, and transaction history.
#
# **Expected Output:**
# - The system should include a user interface (text-based is fine) for:
#   - Members to interact (search, borrow, return books).
#   - Librarians to manage the library and members.
#
# Let me know if you need any clarifications!

## My Code:
class Books:
    def __init__(self, book_id, title, author, genre, quantity, publication_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.publication_year = publication_year

    def search_books(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass


class Members:
    def __init__(self, member_id, name, email, address):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.address = address
        self.borrowed_books = []

class Librarians:
    def add_members(self):
        pass

    def add_books(self):
        pass

    def remove_books(self):
        pass


