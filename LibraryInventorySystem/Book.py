class Book:
    def __init__(self, book_id, title, author, year_published):
        self.book_id = str(book_id)
        self.title = title
        self.author = author
        self.year_published = year_published
 
    def to_dict(self):
        """Converts the object data to a dictionary for JSON serialization."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year_published": self.year_published
        }
 
    @classmethod
    def from_dict(cls, data):
        """Creates a Book instance from a dictionary."""
        return cls(data["book_id"], data["title"], data["author"], data["year_published"])
 