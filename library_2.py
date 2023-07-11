import library_1 as library


while True:
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Loan a book")
    print("4. Return a book")
    print("5. Check if a book is in the library")
    print("6. Show all books in the library")
    print("7. Show all borrowed books and their due dates")
    print("8. Show all books by a certain author")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book publication year: ")
        library.add_book(title, author, year)
    elif choice == 2:
        title = input("Enter book title to get removed from library: ")
        library.remove_book(title)
    elif choice == 3:
        title = input("Enter book title: ")
        borrower = input("Enter book borrower: ")
        days = input("Enter loaning duration (leave blank for 14): ")  
        if days != "":              
            library.loan_book(title,borrower,days)
        else:
            library.loan_book(title,borrower)
    elif choice == 4:
        title = input("Enter book title: ")
        library.return_book(title)
    elif choice == 5:
        title = input("Enter book title: ")
        library.is_in_library(title)
    elif choice == 6:        
        library.show_library()
    elif choice == 7:
         library.show_loans()
    elif choice == 8:
        author = input("Enter book author: ")
        library.show_books_by_author(author)
    elif choice == 9:
        print("Exiting the program. Have a nice day!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 9.")