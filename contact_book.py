# Contact Book App

contacts = []

print("Welcome to your Contact Book!")

while True:
    print("\nMenu:")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Remove contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if not contacts:
            print("No contacts found.")
        else:
            print("Your contacts:")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['name']} - Phone: {contact['phone']}, Email: {contact['email']}")
    elif choice == "2":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print(f"Contact '{name}' added!")
    elif choice == "3":
        search_name = input("Enter the name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print(f"Found: {contact['name']} - Phone: {contact['phone']}, Email: {contact['email']}")
                found = True
        if not found:
            print("Contact not found.")
    elif choice == "4":
        remove_name = input("Enter the name of the contact to remove: ")
        removed = False
        for contact in contacts:
            if contact["name"].lower() == remove_name.lower():
                contacts.remove(contact)
                print(f"Contact '{remove_name}' removed!")
                removed = True
                break
        if not removed:
            print("Contact not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-5.")

