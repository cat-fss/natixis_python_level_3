'''
Class 3 Exercises - Python L3
'''

'''
Exercise 1

Initialize a Git repository, track a file, and make your first commit.

1. Create a new directory with the name "library-project". 
2. Navigate to this project folder.
3. Run the the necessary commands
4. Create a remote repository on GitHub (same name as this folder)
5. Link it to your local repo and push the changes:

# Expected outcome: Your repository should now appear on GitHub.
'''

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

'''
Exercise 8
Display the library collection dynamically in Streamlit and visualize how many times each book has been requested.

1. Create a new file in your project folder named app.py
2. Open app.py and import Streamlit and your Library and Book classes
3. Create a Library instance and add a few books to it (you can hardcode them or reuse the ones from your main script).
4. Convert your book collection into a Pandas DataFrame
5. Display the table
6. Add a simple bar chart to visualize how many times each book has been requested
7. Add a short introductory message at the top with "This dashboard shows how often each book has been requested."
8. Run your app.
'''

'''
Exercise 9

Make the Streamlit app interactive by allowing users to "request" a book.

1. In app.py, add a new section below the bar chart:
   - Use st.selectbox() to let the user choose a book title.
   - Use st.button() to simulate a request for that book.

2. When the button is clicked:
   - Call library.request_book(selected_title) to increment the counter.
   - Recreate the DataFrame and refresh the displayed table and chart.

3. To ensure the counter updates in real time, use Streamlit’s session state:
   python
   if "library" not in st.session_state:
       st.session_state.library = Library()
   library = st.session_state.library

4. After updating, display a confirmation message (e.g., "Book requested successfully!").

5. Stage and commit your work

HINT: use st.session_state
'''

'''
Exercise 10

Add functionality to insert new books directly through the Streamlit interface.

1. Below your existing components, add a form that allows users to enter details for a new book:
   - Use st.text_input() for title, author, and ISBN.
   - Use st.number_input() for the initial number of requests (optional).
   - Add a button labelled “Add Book”.

2. When the user clicks the button:
   - Create a new Book instance.
   - Add it to the library using library.add_book().
   - Display a confirmation message.

3. Recreate the DataFrame to reflect the new addition.

4. Stage and commit your work
'''

''' 
Exercise 11

1. Customize the appearance and layout of your Streamlit app using configuration settings using st.set_page_config.
2. Add a sidebar section with basic information.
3. Test different layouts: "centered" vs "wide"; "expanded" vs "collapsed"
4. Optionally, add your name or course info to the sidebar.
5. Stage and commit your change
'''

'''
Exercise 12
Customize the bar chart in your Streamlit app using Matplotlib for more control over colors and appearance.
'''

'''
Exercise 13
Customize the App Using Streamlit Themes
'''

'''
Exercise 14
Push your completed project to GitHub.
'''