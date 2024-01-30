class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Library books:")
            for book in self.books:
                book.display_info()


# Crearea unei instanțe de bibliotecă
library = Library()

# Introducerea cărților de către utilizator
while True:
    title = input("Introduceți titlul cărții sau 'exit' pentru a ieși: ")
    if title.lower() == 'exit':
        break
    author = input("Introduceți autorul cărții: ")

    book = Book(title, author)
    library.add_book(book)

# Afișarea cărților din bibliotecă
library.display_books()
