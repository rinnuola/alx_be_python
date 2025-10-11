# book_class.py
# Objective: Demonstrate Python magic methods using a Book class

class Book:
    # Constructor (__init__) initializes object attributes when a new instance is created
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor (__del__) runs automatically when an object is deleted
    # It can be used to clean up resources or display a message
    def __del__(self):
        print(f"Deleting {self.title}")

    # __str__ provides a readable (informal) string representation for end users
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # __repr__ provides an official string representation for developers
    # It should return a string that could recreate the same object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
