# Exercise on class 
# =====================
# Book Class:
# Attributes:
# title,author,isbn ,copies (number of available copies)

# Methods:
# add_book(book): Adds a book to the library's collection.
# remove_book(isbn): Removes a book from the library based on its ISBN.
# find_book(isbn): Finds and returns a book based on its ISBN.
# display_books(): Prints the details of all books in the library.

class Book:
    def __init__(self):
        self.lib = []
        print("created new library")
    def add_book(self):
        self.title = input("Enter title of book: ")
        self.author = input("Enter author of book: ")
        self.isbn = input("Enter isbn of book: ")
        self.copies = input("Enter copies of book: ")
        details = {'title' : self.title,
                   'author' : self.author,
                   'isbn' : self.isbn,
                   'copies' : self.copies}
        self.lib.append(details)
        print("\nBook successfully added to library")
    def display_books(self):
        if not self.lib:
            print("\nNo books in the library.")
            return
        print("\nThe books in the library are:\n")
        for book in self.lib:
            print(book)
    def remove_book(self):
        isbn = input("Enter ISBN to remove book: ")
        for book in self.lib:
            if book['isbn'] == isbn:
                self.lib.remove(book)
                print("\nBook removed successfully.")
                return
        print("\nBook not found.")
    def find_book(self):
        isbn = input("Enter ISBN to find book: ")
        for book in self.lib:
            if book['isbn'] == isbn:
                print(f"\nBook Found -> Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")
                return
        print("\nBook not found.")
i = 99
b = Book()
while(i != 0):

    print("\noptions: \n 1:add book \n 2:display book \n 3:find book \n 4:remove book \n enter 0 to exit")
    i = int(input("\nenter an option:"))
    if i == 1:
        b.add_book()
    elif i == 2:
        b.display_books()
    elif i == 3:
        b.find_book()
    elif i == 4:
        b.remove_book()





    
        