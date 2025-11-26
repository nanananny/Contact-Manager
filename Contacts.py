contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added.")

def search_contact(name):
    return contacts.get(name, "Not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Deleted.")
    else:
        print("Contact not found.")

def display_contacts():
    for name in sorted(contacts.keys()):
        print(f"{name}: {contacts[name]}")

while True:
    print("\n1. Add\n2. Search\n3. Delete\n4. Show All\n5. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_contact(input("Name: "), input("Number: "))
    elif ch == "2":
        print(search_contact(input("Name: ")))
    elif ch == "3":
        delete_contact(input("Name: "))
    elif ch == "4":
        display_contacts()
    else:
        break
