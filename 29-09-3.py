# Write program to manage a small lbrary using a dictionary. the program must repeatedly allow the user to add books
# issue books ,return books , display the current book record 
# Conditions :
 
# - Store book title as the key and available copies as the value
# - A book can be issued only if it exists and atleast one is available 
# - Return a book only if already exist in the library record
# - Book names should word regardless of uppercase or lowercase letterslibrary = {}
library = {}
while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ").lower()
        copies = int(input("Enter number of copies: "))

        if book in library:
            library[book] = library[book] + copies
        else:
            library[book] = copies

        print("Book added")

    elif choice == 2:
        book = input("Enter book name: ").lower()

        if book in library and library[book] > 0:
            library[book] = library[book] - 1
            print("Book issued")
        else:
            print("Book not available")

    elif choice == 3:
        book = input("Enter book name: ").lower()

        if book in library:
            library[book] = library[book] + 1
            print("Book returned")
        else:
            print("Book does not exist")

    elif choice == 4:
        print("Current Book Record:")

        for book, copies in library.items():
            print(book, ":", copies)

    elif choice == 5:
        break

    else:
        print("Invalid choice")