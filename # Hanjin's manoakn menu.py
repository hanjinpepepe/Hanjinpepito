# Hanjin's manoakn menu

total_bill = 0
def function():
    qty = int(input("Quantity: "))
    total_bill += qty * 95
    print(f"{qty} chickenjoy added.")

def chickenjoy():
    global total_bill
    qty = int(input("Quantity: "))
    total_bill += qty * 95
    print(f"{qty} chickenjoy added.")

def adobo():
    global total_bill
    qty = int(input("Quantity: "))
    total_bill += qty * 120
    print(f"{qty} adobo added.")

def hotdog_ni_tommy():
    global total_bill
    qty = int(input("Quantity: "))
    total_bill += qty * 80
    print(f"{qty} hotdog_ni_tommy added.")

def pusit():
    global total_bill
    qty = int(input("Quantity: "))
    total_bill += qty * 100
    print(f"{qty} pusit added.")

def talaba():  
    global total_bill
    qty = int(input("Quantity: "))
    total_bill += qty * 110
    print(f"{qty} talaba added.")

def Bird():
    global total_bill
    qty = int(input("Quantity: "))
    total_bill += qty * 150
    print(f"{qty} Bird added.")

while True:
    print("Welcome to Hanjin's Manokan")
    print("1. chickenjoy")
    print("2. adobo")
    print("3. hotdog_ni_tommy")
    print("4. pusit")
    print("5. talaba")
    print("6. Bird")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue

    if choice == 1:
        chickenjoy()
    elif choice == 2:
        adobo()
    elif choice == 3:
        hotdog_ni_tommy()
    elif choice == 4:
        pusit()
    elif choice == 5:
        talaba()
    elif choice == 6:
        Bird()
    elif choice == 7:
        print(f"Total bill: {total_bill}")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")