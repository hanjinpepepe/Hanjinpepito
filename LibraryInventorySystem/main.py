import sys
from Book import Book            # Updated import
from FileHandler import load_books, save_books  # Updated import
 
def display_menu():
    print("\n" + "="*30)
    print("  LIBRARY BOOK INVENTORY SYSTEM")
    print("="*30)
    print("1. Add Book")
    print("2. Display All Books")
    print("3. SEARCH BOOK BY ID")
    print("4. Exit")
    print("="*30)
 
def add_book(books_list):
    print("\n--- ADD NEW BOOK ---")
    book_id = input("Enter Book ID: ").strip()
   
    if any(book.book_id == book_id for book in books_list):
        print("[Error] A book with this ID already exists!")
        return
 
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author: ").strip()
    year_published = input("Enter Year Published: ").strip()
 
    new_book = Book(book_id, title, author, year_published)
    books_list.append(new_book)
    print(f"\n[Success] '{title}' has been added to the local inventory.")
 
def display_all_books(books_list):
    print("\n--- DISPLAY ALL BOOKS ---")
    if not books_list:
        print("No records found in inventory.")
        return
 
    print(f"{'BOOK ID':<12} | {'BOOK TITLE':<30} | {'AUTHOR':<25} | {'YEAR PUBLISHED':<14}")
    print("-" * 90)
    for book in books_list:
        print(f"{book.book_id:<12} | {book.title:<30} | {book.author:<25} | {book.year_published:<14}")
 
def binary_search_books(books_list, target_id):
    """Sorts records by Book ID and runs Binary Search."""
    books_list.sort(key=lambda x: x.book_id)
 
    low = 0
    high = len(books_list) - 1
 
    while low <= high:
        mid = (low + high) // 2
        mid_book = books_list[mid]
 
        if mid_book.book_id == target_id:
            return mid_book
        elif mid_book.book_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
 
    return None
 
def search_book_interface(books_list):
    print("\n--- SEARCH BOOK BY ID ---")
    if not books_list:
        print("Inventory is empty. Add books first.")
        return
 
    target_id = input("Enter the Book ID to look up: ").strip()
    found_book = binary_search_books(books_list, target_id)
 
    if found_book:
        print("\n[MATCH FOUND]:")
        print(f"-> Book ID:       {found_book.book_id}")
        print(f"-> Title:         {found_book.title}")
        print(f"-> Author:        {found_book.author}")
        print(f"-> Year:          {found_book.year_published}")
    else:
        print(f"\n[Not Found] No book matches ID: {target_id}")
 
def main():
    books_inventory = load_books()
 
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
 
        if choice == "1":
            add_book(books_inventory)
        elif choice == "2":
            display_all_books(books_inventory)
        elif choice == "3":
            search_book_interface(books_inventory)
        elif choice == "4":
            save_books(books_inventory)
            print("Terminating application. Goodbye!")
            sys.exit()
        else:
            print("[Invalid Option] Please enter a number from 1 to 4.")
 
if __name__ == "__main__":
    main()
 