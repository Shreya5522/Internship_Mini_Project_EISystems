
import json
import os

FILE = "contacts.json"


def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contact added yet")
        return

    print("\n--------- Contacts ---------")

    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']}\t{c['phone']}\t{c['email']}")


def search_contact():
    search = input("Enter the name to search: ").lower()

    contacts = load_contacts()
    results = []

    for c in contacts:
        if search in c["name"].lower():
            results.append(c)

    if results:
        print("\n--------- Search Results ---------")

        for c in results:
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print()
    else:
        print("No contact found")


while True:
    print("\n--------- Phone Book Manager ---------")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")
    print("--------------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Thank you for using Phone Book Manager!")
        break

    else:
        print("Invalid choice, try again")