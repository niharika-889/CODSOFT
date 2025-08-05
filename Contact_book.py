contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    if name == "" or phone == "":
        print("Name and Phone Number are required!\n")
        return

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}")
    print()

def search_contact():
    key = input("Enter Name or Phone Number to search: ").strip()
    found = False
    for name, info in contacts.items():
        if key.lower() == name.lower() or key == info["Phone"]:
            print(f"\nContact Found - {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter Name to update: ").strip()
    if name in contacts:
        print("Leave blank to keep existing info.")
        phone = input("New Phone Number: ").strip() or contacts[name]["Phone"]
        email = input("New Email: ").strip() or contacts[name]["Email"]
        address = input("New Address: ").strip() or contacts[name]["Address"]

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter Name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print("Contact not found.\n")

def main_menu():
    while True:
        print("======= Contact Book Menu =======")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("====================================")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option. Please try again.\n")
main_menu()