# Part B - Shopping List Manager
shopping_list = []

while True:
    print("\nMenu: add / remove / show / done")
    choice = input("What would you like to do? ").strip().lower()

    if choice == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' added to your list.")
        else:
            print("Please enter a valid item.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your list.")

        else:
            print("That item is not on your list .")

    elif choice == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\nYour shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
    elif choice == "done":
        print("Goodbye! Thank for using shopping list Manager.")
        break
    else:
        print("Invalid choice. Please type add, remove,show,or done")