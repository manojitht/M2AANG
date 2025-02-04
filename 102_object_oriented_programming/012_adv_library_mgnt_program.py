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
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.librarians = {}
        self.members = {}

    def search_book(self):
        pass


class Books:
    def __init__(self, book_id, title, author, genre, quantity, publication_year, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.publication_year = publication_year
        self.status = status

    def __str__(self):
        return f"Id: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Quantity: {self.quantity}, Year: {self.publication_year}."


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Librarians(Person):
    generate_book_id = 0
    generate_member_id = 0
    def __init__(self, librarian_id, name, email):
        super().__init__(name, email)
        self.librarian_id = librarian_id

    @classmethod
    def add_members(cls, name: str, email: str, address: str, library: object):
        cls.generate_member_id += 1
        new_member = Members(cls.generate_member_id, name, email, address)
        library.members[cls.generate_member_id] = new_member
        print(f"New member '{name}' added to the Library successfully!")

    @staticmethod
    def remove_member(member_id: int, library: object):
        if member_id in library.members.keys():
            library.members.pop(member_id)
            print(f"Member removed from the library successfully!")
        else:
            print(f"Member not found, please check!")

    @classmethod
    def add_book(cls, title: str, author: str, genre: str, quantity: int, publication_year: int, library: object, status="available"):
        cls.generate_book_id += 1
        new_book = Books(cls.generate_book_id, title, author, genre, quantity, publication_year, status)
        library.books[cls.generate_book_id] = new_book
        print(f"New book '{title}' added to the Library successfully!")

    @staticmethod
    def remove_book(book_id: int, library: object):
        if book_id in library.books.keys():
            library.books.pop(book_id)
            print(f"Book removed from the library successfully!")
        else:
            print(f"Book not found, please check!")


class Members(Person):
    def __init__(self, member_id, name, email, address):
        super().__init__(name, email)
        self.member_id = member_id
        self.address = address
        self.borrowed_books = {}

    @staticmethod
    def borrow_book(book_id: int, member_id: int, library: object):
        member = library.members[member_id]
        if len(member.borrowed_books) <= 5:
            if book_id in library.books.keys():
                selected_book = library.books[book_id]
                if selected_book.status == "available":
                    selected_book.status = "borrowed"
                    member.borrowed_books[selected_book.title] = datetime.now()
                    print(f"The book '{selected_book.title}' was borrowed from library by {member.name}!")
                    print(member.borrowed_books)
                else:
                    print(f"The book '{selected_book.title}' was already borrowed.")
            else:
                print(f"The books is not in library, please check!")
        else:
            print(f"You've already borrowed {len(member.borrowed_books)} books, only 5 books is allowed to borrow.")

    @staticmethod
    def return_book(book_id: int, member_id: int, library: object):
        member = library.members[member_id]
        if book_id in library.books.keys():
            selected_book = library.books[book_id]
            if selected_book.status == "borrowed":
                selected_book.status = "available"
                member.borrowed_books.pop(selected_book.title)
                print(f"The book '{selected_book.title}' was returned to the library by {member.name}!")
                print(member.borrowed_books)
            else:
                print(f"The book '{selected_book.title}' was already returned.")
        else:
            print(f"The books is not in library, please check!")


    def overdue_tracking(self):
        pass

    def notification(self):
        pass


library = Library()
Librarians.add_members("Manojith", "manojith@gmail.com", "647 1/1, Aluthmawatha Road, Colombo - 15", library)
Librarians.add_members("Kisho Kumar", "kisho@gmail.com", "647 1/1, Aluthmawatha Road, Colombo - 15", library)
Librarians.add_book("Cracking the Coding Interview", "Gayle Laakmann", "Technology", 5, 2000, library)
Librarians.add_book("Python for Automation", "Joe Laakmann", "Technology", 5, 2000, library)
Members.borrow_book(1, 1, library)
Members.borrow_book(1, 2, library)
Members.return_book(1, 1, library)





