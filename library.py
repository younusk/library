import unittest

# Book Class
class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}, Available: {self.available}"

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.title}' has been returned and is now available.")
        else:
            print(f"'{self.title}' is already available.")

# User Class
class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.available:
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{book.title}' added to the library.")
        else:
            print(f"Book with ISBN {book.isbn} already exists in the library.")

    def remove_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' has been removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def add_user(self, user: User):
        if user not in self.users:
            self.users.append(user)
            print(f"User '{user.name}' added to the library.")
        else:
            print(f"User with ID {user.user_id} already exists.")

    def remove_user(self, user_id: str):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"User '{user.name}' has been removed from the library.")
                return
        print(f"User with ID {user_id} not found.")

    def borrow_book(self, user_id: str, isbn: str):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        
        if user and book:
            user.borrow_book(book)
        else:
            if not user:
                print(f"User with ID {user_id} not found.")
            if not book:
                print(f"Book with ISBN {isbn} not found.")

    def return_book(self, user_id: str, isbn: str):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        
        if user and book:
            user.return_book(book)
        else:
            if not user:
                print(f"User with ID {user_id} not found.")
            if not book:
                print(f"Book with ISBN {isbn} not found.")

    def list_available_books(self):
        print("Available books in the library:")
        available_books = [book for book in self.books if book.available]
        if available_books:
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books are currently available.")

# Example usage:
if __name__ == "__main__":
    # Create library
    library = Library()

    # Add books
    book1 = Book(title="The Outsiders", author="S.E. Hinton", isbn="978-0142407332")
    book2 = Book(title="Pride & Prejudice", author="Jane Austen", isbn="978-0486284736")
    library.add_book(book1)
    library.add_book(book2)

    # Add users
    user1 = User(name="Devlin Sparr", user_id="U12345")
    user2 = User(name="Rachel Wallace", user_id="U67890")
    library.add_user(user1)
    library.add_user(user2)

    # Borrow and return books
    library.borrow_book(user_id="U12345", isbn="978-0486284736")
    library.list_available_books()
    library.return_book(user_id="U12345", isbn="978-0486284736")
    library.list_available_books()
class TestBook(unittest.TestCase):
    
    def test_create_book(self):
        book = Book("1984", "George Orwell", "978-0451524935")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.isbn, "978-0451524935")
        self.assertTrue(book.available)
    
    def test_borrow_book(self):
        book = Book("1984", "George Orwell", "978-0451524935")
        book.borrow_book()
        self.assertFalse(book.available)
    
    def test_return_book(self):
        book = Book("1984", "George Orwell", "978-0451524935")
        book.borrow_book()  # Borrow the book
        book.return_book()  # Return the book
        self.assertTrue(book.available)


class TestUser(unittest.TestCase):

    def test_borrow_book(self):
        user = User("Devlin Sparr", "U12345")
        book = Book("1984", "George Orwell", "978-0451524935")
        user.borrow_book(book)
        self.assertIn(book, user.borrowed_books)
        self.assertFalse(book.available)

    def test_return_book(self):
        user = User("Devlin Sparr", "U12345")
        book = Book("1984", "George Orwell", "978-0451524935")
        user.borrow_book(book)
        user.return_book(book)
        self.assertNotIn(book, user.borrowed_books)
        self.assertTrue(book.available)

    def test_view_borrowed_books(self):
        user = User("Devlin Sparr", "U12345")
        book1 = Book("1984", "George Orwell", "978-0451524935")
        book2 = Book("Pride & Prejudice", "Jane Austen", "978-0486284736")
        user.borrow_book(book1)
        user.borrow_book(book2)
        self.assertEqual(len(user.borrowed_books), 2)


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("Pride & Prejudice", "Jane Austen", "978-0486284736")
        library.add_book(book)
        self.assertIn(book, library.books)

    def test_remove_book(self):
        library = Library()
        book = Book("Pride & Prejudice", "Jane Austen", "978-0486284736")
        library.add_book(book)
        library.remove_book("978-0486284736")
        self.assertNotIn(book, library.books)

    def test_add_user(self):
        library = Library()
        user = User("Devlin Sparr", "U12345")
        library.add_user(user)
        self.assertIn(user, library.users)

    def test_remove_user(self):
        library = Library()
        user = User("Devlin Sparr", "U12345")
        library.add_user(user)
        library.remove_user("U12345")
        self.assertNotIn(user, library.users)


# Run the tests
if __name__ == '__main__':
    unittest.main()

