contacts = []

def get_phone():
    while True:
        phone = input("Phone (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("Invalid phone number")

def get_email():
    while True:
        email = input("Email: ").strip()
        if "@" in email and ".com" in email and not email.startswith("@") and not email.endswith("@") and not email.startswith(".") and not email.endswith("."):
            return email
        print("Invalid email format")

def add_contact():
    name = input("Name: ").strip()
    phone = get_phone()
    for c in contacts:
        if c["phone"] == phone:
            print("Phone number already exists")
            return
    email = get_email()
    address = input("Address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully")

def view_contacts():
    if not contacts:
        print("No contacts available")
        return
    print("\nSaved Contacts")
    print("-" * 40)
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']:<20} {c['phone']}")

def find_matches(key):
    key = key.lower()
    matches = []
    for i, c in enumerate(contacts):
        if key in c["name"].lower() or key in c["phone"]:
            matches.append(i)
    return matches

def choose_contact(matches):
    if len(matches) == 1:
        return matches[0]
    print("\nMultiple contacts found:")
    for i, idx in enumerate(matches, 1):
        c = contacts[idx]
        print(f"{i}. {c['name']} - {c['phone']}")
    while True:
        choice = input("Select contact number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            return matches[int(choice) - 1]
        print("Invalid selection")

def search_contact():
    key = input("Enter name or phone: ").strip()
    matches = find_matches(key)
    if not matches:
        print("Contact not found")
        return
    for idx in matches:
        c = contacts[idx]
        print("\nName:", c["name"])
        print("Phone:", c["phone"])
        print("Email:", c["email"])
        print("Address:", c["address"])

def update_contact():
    key = input("Enter name or phone to update: ").strip()
    matches = find_matches(key)
    if not matches:
        print("Contact not found")
        return
    idx = choose_contact(matches)
    contacts[idx]["phone"] = get_phone()
    contacts[idx]["email"] = get_email()
    contacts[idx]["address"] = input("New address: ").strip()
    print("Contact updated")

def delete_contact():
    key = input("Enter name or phone to delete: ").strip()
    matches = find_matches(key)
    if not matches:
        print("Contact not found")
        return
    idx = choose_contact(matches)
    removed = contacts.pop(idx)
    print(f"Deleted: {removed['name']} - {removed['phone']}")

while True:
    print("\n" + "=" * 40)
    print("            CONTACT BOOK")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("-" * 40)

    choice = input("Select option: ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book")
        break
    else:
        print("Invalid option")
