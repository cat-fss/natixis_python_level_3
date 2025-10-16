class Library:
    def __init__(self):
        self.books = []

    # original version
    # def add_book(self, book):
    #     self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Displaying all books in the library:")
        for book in self.books:
            book.display()

    # exercise 3
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display()
                return
        return "Book not found"
    
    # exercise 4
    def add_book(self, book):
        for existing in self.books:
            if existing.isbn == book.isbn:
                print("Book with this ISBN already exists.")
                return
        self.books.append(book)

    # exercise 5
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return "Book removed."
                return
        return "Book not found."

    # exercise 7
    def request_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.times_requested += 1
                return(f"Book '{book.title}' has been requested.")
        return "Book is not available (yet!)"