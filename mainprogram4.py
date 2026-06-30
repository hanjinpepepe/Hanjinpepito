from inherit4 import PrintedBook, EBook
def binary_search_isbn(book_list, target_isbn):
    """
    Implements the Binary Search algorithm to search for a book using its ISBN.
    """
    low = 0
    high = len(book_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_isbn = book_list[mid].get_isbn() 
        
        if mid_isbn == target_isbn:
            return book_list[mid]
        elif mid_isbn < target_isbn:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

def main():
    library_catalog = [] 
    print("--- Library Management System ---")
    try:
        num_books = int(input("Enter the number of books to add to the catalog: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    for i in range(num_books):
        print(f"\n[Enter Details for Book {i + 1}]")
        book_type = input("Choose book type (1 for Printed Book, 2 for E-Book): ") 
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        
        if book_type == '1':
            pages = int(input("Number of Pages: "))  
            book = PrintedBook(title, author, isbn, pages)
            library_catalog.append(book)
            
        elif book_type == '2':
            size = float(input("File Size (MB): "))     
            book = EBook(title, author, isbn, size)
            library_catalog.append(book)
            
        else:
            print("Invalid choice. Skipping this entry.")

    library_catalog.sort(key=lambda b: b.get_isbn())
    print("\n==========================================")
    print("ALL BOOKS IN CATALOG (SORTED BY ISBN)")
    print("==========================================")
    for book in library_catalog:
        book.display_info()       
    print("==========================================\n")
    target_isbn = input("Enter an ISBN to search for a specific book: ")
    found_book = binary_search_isbn(library_catalog, target_isbn)
    
    if found_book:
        print("\n--- Book Found! ---")
        found_book.display_info()
    else:
        print("\nBook not found.")

if __name__ == "__main__":
    main()