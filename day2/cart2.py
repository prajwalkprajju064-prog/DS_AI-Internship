cart = {}

while True:
    print("\n1. Add fruit")
    print("2. View cart")
    print("3. Update quantity")
    print("4. Remove fruit")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":  # Create
        fruit = input("Fruit name: ")
        qty = int(input("Quantity: "))
        cart[fruit] = qty
        print(f"{fruit} added.")

    elif choice == "2":  # Read
        print("Cart:", cart)  

    elif choice == "3":  # Update
        fruit = input("Fruit to update: ")
        if fruit in cart:
            qty = int(input("New quantity: "))
            cart[fruit] = qty
            print(f"{fruit} updated.")
        else:
            print("Fruit not found.")

    elif choice == "4":  # Delete
        fruit = input("Fruit to remove: ")
        if fruit in cart:
            del cart[fruit]
            print(f"{fruit} removed.")
        else:
            print("Fruit not found.")

    elif choice == "5":  # Exit
        print("Final Cart:", cart)
        break

    else:
        print("Invalid choice.")
