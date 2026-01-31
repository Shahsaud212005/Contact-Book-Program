contacts = {}

def add_contact():
    name = input("Enter the person's name: ")
    number = input("Enter the person's contact number: ")
    contacts[name] = number
    print("Contact added successfully.")

def display_contacts():
    if not contacts:
        print("There are no contacts in the list yet. Please add some first.")
    else:
        print("\n--- Contact List ---")
        for name, number in contacts.items():
            print(f"Name: {name}, Contact Number: {number}")

def delete_contact():
    while True:
        choice = input("Delete 'single' contact or 'all'? ").lower()
        if choice == "all":
            contacts.clear()
            print("All contacts have been deleted.")
            break
        elif choice == "single":
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print(f"No contact found with the name '{name}'.")
            break
        else:
            print("Invalid input. Please enter 'single' or 'all'.")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Name: {name}, Contact: {contacts[name]}")
    else:
        print(f"No contact found with the name '{name}'.")

def update_contact():
    while True:
        choice = input("Update 'name' or 'contact'? ").lower()
        if choice == "name":
            old_name = input("Enter the current name: ")
            if old_name in contacts:
                new_name = input("Enter the new name: ")
                contacts[new_name] = contacts.pop(old_name)
                print("Name updated.")
            else:
                print(f"No contact found with the name '{old_name}'.")
            break
        elif choice == "contact":
            name = input("Enter the name whose contact you want to update: ")
            if name in contacts:
                new_number = input("Enter the new contact number: ")
                contacts[name] = new_number
                print("Contact number updated.")
            else:
                print(f"No contact found with the name '{name}'.")
            break
        else:
            print("Invalid input. Please choose 'name' or 'contact'.")

def contact_book_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

# Run the contact book
contact_book_menu()
