def add_contacts():
    
    name = input("Enter the person's name: ")
    number = input("Enter the person's contact number: ")
    contacts[name] = number
    print("Contact  added successfully.")
    

def display_contacts():

    if len(contacts) == 0:
        print("There are no contacts in the list yet. First add some contacts.")
    else:
        print("Here is the contact list.")
        for key,value in contacts.items():
            print(f"Name = {key},Contact number = {value}")
    
    

def delete_contacts():

    while True:

        delete = input("Do you want to delete all contacts or a single contact? (select 'single' for one contact and 'all' for all contacts): ").lower()

        if delete == "all":
            contacts.clear()

        elif delete == "single":
            delete_single = input("Enter the name of the contact you want to delete: ")    
            if delete_single not in contacts:
                print(f"Name {delete_single} is not in contacts.")
            else:
                contacts.pop(delete_single)
                print("Contact Deleted.")
                
        else:
            print("I don't understand, Select only between single and all to delect contacts.")
    
def search_contacts(): 
    
    search_contact = input("Enter the name of the person you want to search: ")

    if search_contact not in contacts:
        print(f"Name {search_contact} is not in contacts.")
    elif search_contact in contacts:
        print("Here are the person's contact details.")
        print(f"Name = {search_contact}, Contact = {contacts[search_contact]}")
        

def update_contacts():
    
    while True:
        task_2 = input("What do you want to update in the list, A person's name or contact?").lower()

        if task_2 == "name":
            old_name = input("Enter the name of the person you want to update: ")
            
            if old_name not in contacts:
                print(f"Name {old_name} is not in contacts.")
            else:
                new_name = input("Enter the new name for this person: ")
                contacts[new_name] = contacts[old_name]
                del contacts[old_name]
                print("Name updated.")
                
        elif task_2 == "contact":
            old_contact = input("Enter the name of the person whose contact you want to update: ")
            
            if old_contact not in contacts:
                print(f"Name {old_contact} is not in contacts.")
            else:
                new_contact = input("Enter the new contact for this person: ")
                contacts[old_contact] = new_contact
                print("Contact updated.")
                
        else:
            print("I don't understand, Select only between name or contact")


def Menu():
    while True:
        Task = input("Welcome to the Contactbook! \nSelect from the following options (Carefull !, only select the number of the option from the following)"
    "\n1) Add Contacts"
    "\n2) Search Contacts"
    "\n3) Update Contacts"
    "\n4) Delete Contacts"
    "\n5) Display Contacts"
    "\n: ").lower()


        if Task == "1":
            add_contacts()
        elif Task == "2":
            search_contacts()
        elif Task == "3":
            update_contacts()
        elif Task == "4":
            delete_contacts()
        elif Task == "5":
            display_contacts()
        else:
            print("I don't understand, please select from the given options")

contacts = {}

Menu()