class Contacts(object):
    def __init__(self):
        self.contacts = {}

    def cont(self):
        print("Menu:\n1) Add a Contact\n2) Find a Contact\n3) Exit")
        option = int(input("> "))
        if option == 1:
            print("Enter Name: ")
            contact_name = input("> ")
            print("Enter Number: ")
            contact_number = int(input("> "))
            self.contacts[contact_name] = contact_number
            print("Contact Added")
            self.cont()
        elif option == 2:
            print("Enter name")
            find_name = input("> ")
            if find_name in self.contacts:
                print(self.contacts[find_name])
            else:
                print("No contact found")
            self.cont()
        elif option == 3:
            s = File()
            s.save()
            exit(0)
        else:
            print("BZZEEZZZ")
            self.cont()


class File(object):
    def save(self):
        final_contacts = c.contacts
        file = open("contacts.txt", "w")
        file.write(f"{final_contacts}")
        file.close()


c = Contacts()
c.cont()
c.contacts
