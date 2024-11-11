import os
import re

def read_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = []
            for line in file:
                name, number, email, address = line.strip().split(',')
                temp_name = name.split(':')
                temp_number = number.split(':')
                temp_email = email.split(':')
                temp_address = address.split(':')
                contacts.append({temp_name[0].strip(): temp_name[1].strip(), temp_number[0].strip(): temp_number[1].strip(), temp_email[0].strip(): temp_email[1].strip(), temp_address[0].strip(): temp_address[1].strip()})
            return contacts
    except FileNotFoundError:
        return []
    
def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['number']},{contact['email']},{contact['address']}\n")

def add_contact(contacts, filename):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    new_contact = {'name': name, 'phone number': number, 'email': email, 'address': address}
    contacts.append(new_contact)
    with open(filename, 'a') as file:
        file.write(f"Name: {name}, Phone Number: {number}, Email: {email}, Address: {address}\n")
    print(f"{name} added to contacts")

def edit_contact(contacts, filename):
    contact_to_edit = input("Enter the name of the contact you want to edit: ")
    print(contact_to_edit, contacts)
    for contact in contacts:
        if contact_to_edit in contact['Name']:           
            new_name = input("Enter name: ")
            new_number = input("Enter phone number: ")
            new_email = input("Enter email: ")
            new_address = input("Enter address: ")
            if new_name: contact['Name'] = new_name
            if new_number: contact['Number'] = new_number
            if new_email: contact['Email'] = new_email
            if new_address: contact['Address'] = new_address
            with open(filename, 'w') as file:
                file.write(f"Name: {new_name}, Phone Number: {new_number}, Email: {new_email}, Address: {new_address}")
            print(f"{contact_to_edit} has been updated")

def delete_contact(contacts, filename):
    contact_to_delete = input("Which contact do you eant to delete? ")
    try:
        with open(filename, 'r') as file:
            contacts = file.readlines()
            with open(filename, 'w') as f:
                for contact in contacts:
                    if contact_to_delete.strip('\n') != contact['Name']:
                        f.write(contact)
                        print("Deleted")
    except:
        print("Contact not found")

def search_contact(contacts, filename):
    name = input("Enter the name of the contact to search for: ")
    with open(filename, 'r') as file:
        contacts = file.read()
        for contact in contacts:
            if name in contact[0]:
                print(f"{contact[0]}, {contact[1]}, {contact[2]}, {contact[3]}")

def display_contacts(contacts):
    if not contacts:
        print("There are no contacts.")
    else:
        with open('contacts.txt', 'r'):
            for contact in contacts:
                print(contact)

def export_to_textfile(contacts, filename):
    path = input("Enter the path to the file you would like to export: ")
    os.makedirs(path, exist_ok=True)    
    contacts.append(path)
    with open(filename, 'a') as file:
        file.write(path)

def main():
    contacts = read_contacts('contacts.txt')
    print("Welcome to the Contact Management System!") 


    while True:
        print("Menu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit")
        choice = input("Please enter a number from the list above: ")
        if choice == "1":
            add_contact(contacts, 'contacts.txt')
        elif choice == "2":
            edit_contact(contacts, 'contacts.txt')
        elif choice == "3":
            delete_contact(contacts, 'contacts.txt')
        elif choice == "4":
            search_contact(contacts, 'contacts.txt')
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            export_to_textfile(contacts, 'contacts.txt')
        elif choice == "7":
            break
        else:
            print("Invalid input. Please enter a number from the menu. ")

if __name__ == "__main__":
    main()
        