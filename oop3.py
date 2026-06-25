from abc import ABC, abstractmethod

# ==========================================
# 1. BASE ABSTRACT CLASS
# ==========================================
class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.set_isbn(isbn)

    @abstractmethod
    def read(self):
        pass
    
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        if isbn >= 0:
            self.__isbn = isbn
        else:
            print("ISBN cannot be negative!")
            self.__isbn = 0
    
    @abstractmethod
    def display(self):
        pass