from abc import ABC, abstractmethod


class PrintedBook(Book):
    def __init__(self, title, author, isbn, number_of_pages):
        super().__init__(title, author, isbn)
        self.number_of_pages = number_of_pages

    def read(self):
        print(f"Reading the printed book '{self.title}' by {self.author}.")

    def display(self):
        print(f"Printed Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"Number of Pages: {self.number_of_pages}")


class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size

    def read(self):
        print(f"Reading the ebook '{self.title}' by {self.author}.")

    def display(self):
        print(f"Ebook Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"File Size: {self.file_size} MB")


if __name__ == "__main__":
    printed = PrintedBook("1984", "George Orwell", 1234567890, 328)
    ebook = Ebook("Python 101", "Jane Doe", 987654321, 5)

    printed.display()
    printed.read()
    print()
    ebook.display()
    ebook.read()
