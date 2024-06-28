#CONTACT BOOk

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("\nContact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        if not found_contacts:
            print("\nNo contact found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nContact found. Enter new details.")
                contact.name = input("Enter new name: ")
                contact.phone_number = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("\nContact updated successfully!")
                return
        print("\nContact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("\nContact deleted successfully!")
                return
        print("\nContact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("-------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        option = input("\nEnter your option (1-6): ")

        if option == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif option == '2':
            contact_book.view_contacts()
        elif option == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif option == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)
        elif option == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif option == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
