#Write a menu driven python program where the user can add items, remove items, view cart and exit 
cart = []
while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print("Item added successfully.")

    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            print("Item removed successfully.")
        else:
            print("Item not found in cart.")

    elif choice == 3:
        print("Your cart:", cart)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")