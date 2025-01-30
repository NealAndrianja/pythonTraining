import contact

def main():
    while True:
        print("\n CONTACT MANAGER")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Export contacts")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact.add_contact(name, phone, email, address)
            print(f"Contact {name} saved successfully.")


if __name__ == "__main__":
    main()