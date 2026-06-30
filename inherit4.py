from oop4 import Book

class PrintedBook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.pages = pages
        
    def display_info(self):
        print("\n[PRINTED BOOK INFORMATION]")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"Pages: {self.pages}")
        
        
class EBook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.file_size = file_size
        
    def display_info(self):
        print("\n[E-BOOK INFORMATION]")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"File size: {self.file_size} MB")