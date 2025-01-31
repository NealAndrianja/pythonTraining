import file

contacts = file.readData()
phone_numbers = set()

def add_contact(name, phone, email, address):
    if phone in phone_numbers:
        print("Phone number already exists")
        return

    new_contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(new_contact)
    phone_numbers.add(phone)
    file.writeData(new_contact)

def remove_contact(phone):
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            phone_numbers.remove(phone)
            return

def list_contacts():
    for contact in contacts:
        print(f"{contact['name']}, {contact['phone']}, {contact['email']}, {contact['address']}")
