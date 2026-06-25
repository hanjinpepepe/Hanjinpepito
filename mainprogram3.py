# 3. MAIN PROGRAM (USER INPUT)
# ==========================================
def main():
    print("--- Book Management System ---")
    print("What type of book would you like to create?")
    print("1. Printed Book")
    print("2. Ebook")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice. Exiting program.")
        return

    # Gather common attributes required by the parent class
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    # Simple error handling for numerical inputs
    try:
        isbn = int(input("Enter ISBN (numbers only): "))
    except ValueError:
        print("Invalid input. ISBN must be an integer. Setting to 0.")
        isbn = 0

    # Gather subclass-specific attributes
    if choice == '1':
        try:
            pages = int(input("Enter number of pages: "))
        except ValueError:
            print("Invalid input. Defaulting to 100 pages.")
            pages = 100
        
        # Instantiate PrintedBook
        my_book = PrintedBook(title, author, isbn, pages)

    elif choice == '2':
        try:
            size = float(input("Enter file size in MB: "))
        except ValueError:
            print("Invalid input. Defaulting to 1.0 MB.")
            size = 1.0
            
        # Instantiate Ebook
        my_book = Ebook(title, author, isbn, size)

    # Demonstrate the object works
    my_book.display()
    my_book.read()

if __name__ == "__main__":
    main()