import json
import os
from Book import Book  # Updated import
 
JSON_FILE = "books.json"
 
def load_books():
    """Loads books from the JSON file and returns a list of Book objects."""
    if not os.path.exists(JSON_FILE):
        return []
   
    try:
        with open(JSON_FILE, "r") as file:
            data_list = json.load(file)
            return [Book.from_dict(data) for data in data_list]
    except (json.JSONDecodeError, IOError):
        print("\n[Error] Could not read books.json. Starting with an empty database.")
        return []
 
def save_books(books_list):
    """Saves the list of Book objects permanently to the JSON file."""
    try:
        with open(JSON_FILE, "w") as file:
            json_ready_data = [book.to_dict() for book in books_list]
            json.dump(json_ready_data, file, indent=4)
        print("\n[Success] All book records saved successfully to JSON.")
    except IOError:
        print("\n[Error] Critical error saving records to file.")
 