class Book:
    def __init__(self, title, author, isbn, times_requested=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.times_requested = times_requested  # optional parameter with default

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn} Requested: {self.times_requested} time(s)")

# exercise 6
class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, File size: {self.file_size}MB")