from datetime import datetime, timedelta

x     = 1
books = []
loans = {}

def add_book(title, author, year):
    # books are represented as dictionaries
    book = {
        "title": title,
        "author": author,
        "year":year
        }
    books.append(book)

def remove_book(title):
    for book in books:
        if book['title'] == title:
            books.remove(book)

def loan_book(title, borrower, days=14): #id, maxbooks
    # the due date is todays date plus number of days (default 2 weeks)
    due_date = datetime.now() + timedelta(days=days)
    # recording loan in a 
    loans[title] = {
        "borrower": borrower,
        "due_date": due_date
    }

def return_book(title):
    # simply removing loaned book from loans dictionary
    if title in loans:
        loans.pop(title)

def is_in_library(title):
    for book in books:
        if book["title"] == title:
            print("Yessir book is in library")

def show_library():
    print("I have a fine selection right here: ")
    for book in books:
        print(book)

def show_loans():
    for title, loan_info in loans.items():
        print(f"{title} is borrowed by {loan_info['borrower']} until {loan_info['due_date']}")

def show_books_by_author(author):
    for book in books:
        if book["author"] == author:
            print(book)


print(books)
print("adding some books...")
add_book("Harry Potter","J.K. Rowling","1996")
add_book("Sapiens","Yuval Noah Harari","2014")
add_book("Black Hat Python"," Justin Seitz","2015")
print(books)
print("removing a book...")
remove_book("Harry Potter")
print(books)
print(loans)
print("loaning a book...")
loan_book("Sapiens","John Thomas")
print(books)
print(loans)
print("returning a book...")
return_book("Sapiens")
print(books)
print(loans)
is_in_library("Black Hat Python")
loan_book("Black Hat Python","Markus")
show_library()
show_loans()
show_books_by_author("Yuval Noah Harari")