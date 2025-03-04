class Book:
    def __init__(self):
        self.lib = []
        print("created new library")
    def add_book(self):
        self.title = input("Enter title of book: ")
        self.author = input("Enter author of book: ")
        self.isbn = input("Enter isbn of book: ")
        details = {'title' : self.title,
                   'author' : self.author,
                   'isbn' : self.isbn,}
        self.lib.append(details)
        print("\nBook successfully added to library")
    def display_books(self):
        if not self.lib:
            print("\nNo books in the library.")
            return
        print("\nThe books in the library are:\n")
        for book in self.lib:
            print(book)
i = 99
b = Book()
while(i != 0):

    print("\noptions: \n 1:add book \n 2:display book \n enter 0 to exit")
    i = int(input("\nenter an option:"))
    if i == 1:
        b.add_book()
    elif i == 2:
        b.display_books()






    
        