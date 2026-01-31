def add_contacts(info):
        
        while True:
            name = input("Enter the person's name: ").lower()
            if len(name) > 20:
                print("The contact name can't be longer than 20 characters.")
            elif len(name) <= 0:
                print("The contact name can't be empty.")
            else:
                break

        while True:
            number = input("Enter the person's contact number: ")
            if len(number) <= 0:
                print("The contact number can't be empty.")
            elif (number.isdigit()) == False:
                print("Please type only numbers in the contact section.")
            else:
                break
        
        info[name] = number
        print("Contact added successfully.")
        print("")

def search_contacts(info):

    while True:
        
        if len(contacts) == 0:
            print("There are no contacts in the list yet. Add some first.")
            break
        else:
            search_contact = input("Enter the name of the person you want to search: ").lower()
            if len(search_contact) == 0:
                print("The name can't be empty.")
            elif search_contact not in contacts:
                print(f"Name {search_contact} is not in contacts.")
                print("")
            elif search_contact in contacts:
                print("Here are the person's contact details.")
                print(f"Name = {search_contact.capitalize()}, Contact = {contacts[search_contact]}")
                print("")
                break

def update_contacts(info):
    
    while True:

        if len(contacts) == 0:
            print("There are no contacts in the list yet. Add some first.")
            break
        else:
            task_2 = input("What do you want to update in the list, A person's name or contact?").lower()

            if task_2 == "name":
                old_name = input("Enter the name of the person you want to update: ")
                
                if old_name not in contacts:
                    print(f"Name {old_name} is not in contacts.")
                    print("")
                else:
                    new_name = input("Enter the new name for this person: ").lower()
                    contacts[new_name] = contacts[old_name]
                    del contacts[old_name]
                    print("Name updated.")
                    print("")
                    break
            
            elif task_2 == "contact":
                old_contact = input("Enter the name of the person whose contact you want to update: ")
                
                if old_contact not in contacts:
                    print(f"Name {old_contact} is not in contacts.")
                    print("")
                else:
                    new_contact = ""
                    while new_contact.isdigit() == False:
                        new_contact = input("Enter the new contact for this person: ")
                        print("Enter only numbers in the contact.")
                    else:
                        contacts[old_contact] = new_contact
                        print("Contact updated.")
                        print("")
                        break
                
            else:
                print("I don't understand, Select only between name or contact")

def delete_contacts(info):

    while True:

        if len(contacts) == 0:
            print("There are no contacts in the list yet. Add some first.")
            break
        else:
            delete = input("Do you want to delete all contacts or a single contact? (select 'single' for one contact and 'all' for all contacts): ").lower()

            if delete == "all":
                contacts.clear()
                print("Contacts Deleted.")
                print("")
                break
        
            elif delete == "single":
                delete_single = input("Enter the name of the contact you want to delete: ")    
                if delete_single not in contacts:
                    print(f"Name {delete_single} is not in contacts.")
                    print("")
                else:
                    contacts.pop(delete_single)
                    print("Contact Deleted.")
                    print("")
                    break
        
            else:
                print("I don't understand, Select only between single and all to delete contacts.")

def display_contacts(info):

    if len(contacts) == 0:
        print("There are no contacts in the list yet. Add some first.")
        print("")
    else:
        print("Here is the contact list.")
        print("")
        for key,value in contacts.items():
            print(f"Name = {key.capitalize()}, Contact number = {value}")
        print("")  

def Menu():

    while True:
        print("1) Add Contacts")
        print("2) Search Contacts")
        print("3) Update Contacts")
        print("4) Delete Contacts")
        print("5) Display Contacts")
        print("6) Exit")
        Task = input(": ")

        if Task == "1":
            add_contacts(contacts)
        elif Task == "2":
            search_contacts(contacts)
        elif Task == "3":
            update_contacts(contacts)
        elif Task == "4":
            delete_contacts(contacts)
        elif Task == "5":
            display_contacts(contacts)
        elif Task == "6":
            print("Bye, Thank you for using the program.")
            break
        else:
            print("I don't understand, please select from the given options")

contacts = {}

print("Welcome to the Contactbook! \nSelect from the following options (Carefull !, only select the number of the option from the following)")

Menu()