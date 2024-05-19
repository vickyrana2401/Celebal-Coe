import csv
import os

CONTACTS_FILE = 'contacts.csv'

def create_contacts_file():
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone Number', 'Email', 'Address'])

def add_contact(name, phone_number, email, address):
    with open(CONTACTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone_number, email, address])

def view_contacts():
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

def update_contact(name, new_phone_number=None, new_email=None, new_address=None):
    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                if new_phone_number:
                    row[1] = new_phone_number
                if new_email:
                    row[2] = new_email
                if new_address:
                    row[3] = new_address
            contacts.append(row)

    with open(CONTACTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def delete_contact(name):
    contacts = []
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                contacts.append(row)

    with open(CONTACTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def search_contact(query):
    with open(CONTACTS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if query.lower() in [field.lower() for field in row]:
                print(', '.join(row))

def main():
    create_contacts_file()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number (leave empty to skip): ")
            new_email = input("Enter new email (leave empty to skip): ")
            new_address = input("Enter new address (leave empty to skip): ")
            update_contact(name, new_phone_number, new_email, new_address)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '5':
            query = input("Enter the name or other details to search for: ")
            search_contact(query)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
