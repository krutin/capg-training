class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __add__(self, other):
        new_title = f"{self.title} & {other.title}"
        new_author = f"{self.author} and {other.author}"
        combined_book = Book(new_title, new_author)
        combined_book.display()
        return combined_book

    def display(self):
        print(f"Book: {self.title} by {self.author}")


book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee")

combined_book = book1 + book2