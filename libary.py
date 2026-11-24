import os

if os.getenv("JENKINS_HOME"):
    print("\nJenkins Build Started Successfully!")
    print("Library Management System")
    print("Python program executed successfully.")
else:
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Available Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        try:
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
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

        except EOFError:
            print("Input unavailable.")
            break