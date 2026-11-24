
books = []

def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "status": "Available",
        "student": ""
    }

    books.append(book)
    print("\nBook Added Successfully!")

def display_books():
    print("\n--- Available Books ---")

    found = False
    for book in books:
        if book["status"] == "Available":
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("----------------------")
            found = True

    if not found:
        print("No available books.")

def search_book():
    book_id = input("Enter Book ID to Search: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found!")
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book Not Found!")

def issue_book():
    book_id = input("Enter Book ID to Issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                student = input("Enter Student Name: ")
                book["status"] = "Issued"
                book["student"] = student
                print("\nBook Issued Successfully!")
            else:
                print("Book is Already Issued!")
            return

    print("Book Not Found!")

def return_book():
    book_id = input("Enter Book ID to Return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                book["student"] = ""
                print("\nBook Returned Successfully!")
            else:
                print("Book is Not Issued!")
            return

    print("Book Not Found!")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Available Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("\nThank You! Exiting Library System.")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")
