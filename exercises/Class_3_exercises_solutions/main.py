import os
os.chdir("exercises/Class_3_exercises_solutions")

'''
Python Advanced Course - Level 3 - Exercise Solutions
'''

'''
Exercise 1

Initialize a Git repository, track a file, and make your first commit.

1. Create a new directory with the name library-project. 
2. Navigate to this project folder.
3. Run the the necessary commands
4. Create a remote repository on GitHub (same name as this folder)
5. Link it to your local repo and push the changes:

# Expected outcome: Your repository should now appear on GitHub.
'''

# mkdir library-project
# cd library-project
# git init
# notepad README.md
# git commit -m "First commit"
# git remote add origin <origin_url>
# git push

'''
Exercise 2
Create two Python modules (book.py and library.py) and design simple classes to represent books and a library.
1. In book.py, define a class named Book with:
   - Attributes: title, author, and isbn
   - A method display() that prints the book details in a single line.

2. In library.py, define a class named Library with:
   - An attribute books that stores a list of Book objects.
   - A method add_book() that appends a book to the list.
   - A method display_books() that prints the details of all books in the collection.

3. Create a third file named main.py. In this file:
   - Import both classes (Book and Library).
   - Create a Library instance.
   - Add at least two Book instances to it.
   - Display all books in the library.

4. Run your program to ensure it prints the expected output.
    Expected Output:
        Displaying all books in the library:
        Title: Python Programming, Author: John Doe, ISBN: 1234567890
        Title: Advanced Python, Author: Jane Smith, ISBN: 0987654321

5. Stage and commit your work
'''

# see books.py, library.py
from library import Library
from book import Book

# Create a Library instance
library = Library()

# Add some books
library.add_book(Book("Python Programming", "John Doe", "1234567890"))
library.add_book(Book("Advanced Python", "Jane Smith", "0987654321"))

# Display all books
library.display_books()

# git add .
# git commit -m "added library, book, and main modules"
# git push

'''
Exercise 3
Enhance your Library class with a search functionality to find books by title.

1. Inside the Library class, add a new method named find_book(title):
   - The method should iterate over all stored books.
   - If a book title matches the input (case-insensitive), print its details.
   - If no match is found, return Book not found.

2. In main.py:
   - After displaying all books, call find_book() with the title of one of the books in your collection.
   - Then, call it again with a title that doesn’t exist to test the “not found” case.

3. Run your program to ensure both scenarios work correctly.
'''
# Search for existing and non-existing titles
library.display_books()
library.find_book("Python Programming")
library.find_book("Data Science Essentials")

'''
Exercise 4

Prevent duplicate books from being added to the library.

1. Modify the add_book() method inside the Library class so that:
   - Before adding a new book, it checks whether a book with the same ISBN already exists in the library.
   - If it does, display a message such as: "Book with this ISBN already exists."
   - If it doesn not, add the new book as usual.

2. In main.py:
   - Try adding two books with the same ISBN.
   - Run the program and confirm that the duplicate is rejected.
'''

library.add_book(Book("Python Programming", "John Doe", "1234567890"))
library.add_book(Book("Another Python Book", "Mary Johnson", "1234567890"))  # duplicate
library.add_book(Book("Advanced Python", "Jane Smith", "0987654321"))

library.display_books()

'''
Exercise 5

Add functionality to remove books from the library.

1. Inside the Library class, create a new method called remove_book(isbn):
   - It should search for a book by its ISBN.
   - If the book exists, remove it from the library and print a confirmation message.
   - If it doesn’t exist, return Book not found.

2. In main.py:
   - After adding some books, remove one of them using its ISBN.
   - Try removing an ISBN that doesn't exist to test both cases.
'''

# Remove existing and non-existing books
library.remove_book("1234567890")  # should remove
library.remove_book("9999999999")  # should print "Book not found"

'''
Exercise 6
Inheritance and Polimorphism: Create a subclass for Electronic Books

1. Below the Book class, define a new class called EBook that inherits from Book.

2. The EBook class should:
   - Include all attributes of Book.
   - Add a new attribute called file_size (in MB).
   - Override the display() method to also show the file size.

3. In main.py:
   - Create one EBook instance and one regular Book.
   - Add both to the library.
   - Display all books to confirm that the EBook includes the extra information.

'''
from book import Book, EBook
library.add_book(EBook("Machine Learning Guide", "Sarah Lee", "5678901234", 2.5))

library.display_books()

'''
Exercise 7
Add an optional attribute to track how many times a book has been requested.

1. Modify the Book class so it accepts an additional, optional parameter named times_requested (default value = 0).  
   - Store this parameter as an instance variable.
   - Update the display() method so it also prints the number of times a book has been requested.
2. Modify the Library class to have a new method request_book(title)
   - It should search for a book by title.
   - If found, increment its times_requested count and return a confirmation message.
   - If the book is not found, return Book is not available (yet!)
3. In main.py:
   - Create a few books (some with a predefined times_requested value).
   - Call request_book() a few times to simulate borrowing or requesting books.
   - Display all books to confirm that the counts have been updated correctly.
4. Stage, commit, and push your changes.
'''
library.add_book(Book("Python Programming", "John Doe", "1234567890"))
library.add_book(Book("Python for Dummies", "Hannah Silva", "0111654321", times_requested=10))

# Simulate book requests
library.request_book("Python Programming")
library.request_book("Python Programming")
library.request_book("Advanced Python")
library.request_book("Intermediate Python")
library.request_book("Python for Dummies")

# Display final state
library.display_books()

# git add .
# git commit -m "I'm already up to exercise 7, I'm awesome!"
# git push

