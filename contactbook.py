class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
         return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f" Contact '{name}' has been added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print(" Oops! It looks like you don't have any contacts saved yet.")
            return
        print(" Here’s your contact list:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            print(" Here are the search results:")
            for contact in found_contacts:
                print(contact)
        else:
            print(" Sorry, no contacts found matching your search.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f" Contact '{name}' has been updated successfully.")
                return
        print(f" Sorry, we couldn't find a contact named '{name}'.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"️ Contact '{name}' has been deleted successfully.")
                return
        print(f" Sorry, we couldn't find a contact named '{name}'.")


def main():
    manager = ContactManager()

    while True:
        print("\n Welcome to the Contact Manager!")
        print("1. Create New Contact.")
        print("2. View  Contacts.")
        print("3. Search Contact.")
        print("4. Update an Existing Contact.")
        print("5. Delete  Contact.")
        print("6. Exit Contact Manager.")

        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Number: ")
            email = input("Enter Email Address: ")
            address = input("Enter Address : ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter the name or phone number of the contact you want to find: ")
            manager.search_contact(search_term)

        elif choice == '4':
            name = input("Enter Name Of Contact To Update:")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, new_phone if new_phone else None,
                                   new_email if new_email else None,
                                   new_address if new_address else None)

        elif choice == '5':
            name = input("Which contact would you like to delete? ")
            manager.delete_contact(name)

        elif choice == '6':
            print(" Thank you for using the Contact Manager! Have a great day!")
            break

        else:
            print(" Invalid choice. Please select a valid option (1-6).")

main()