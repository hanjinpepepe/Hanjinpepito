from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
            
    @abstractmethod
    def display_info(self):
        pass   