# Provided for Testing: main.py
# To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods
# from book_class import Book

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected: 1984 by George Orwell, published in 1949

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected: Book('1984', 'George Orwell', 1949)

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()

