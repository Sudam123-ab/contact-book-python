
contacts=[]

def add_contacts():
    
    name=input("Enter a name :")
    if name.strip()=="":
        print("name can not empty")
        return
    for contact in contacts:
        if contact["name"]==name:
            print("Name Already exists!")
            return 
    while True:   
        try: 
            phone=int(input("Enter phone :"))
            break
        except ValueError:
            print("phone must be number only :")
    city=input("Enter city :")

    contacts.append({
                "name":name,
                "phone":phone,
                "city":city
            })    
    print("Contact added!")

def view_contacts():
    if len(contacts)==0:
        print("No contacts found!")
    else:
        for i in range(len(contacts)):
            print(f"{i+1}.{contacts[i]['name']} | {contacts[i]['phone']} | {contacts[i]['city']}")
            
def search_contact():
    name=input("Enter name to search :")
    for contact in contacts:
        if contact["name"]==name:
            print(f"Name: {contact['name']} | phone:{contact['phone'] } | city:{contact['city']}")   
            return 
    print("contact not found!")


def delete_contact():
    name=input("enter to delete:")
    for contact in contacts:
        if contact["name"]==name:
            contacts.remove(contact)
            print("contact deleted!")
            return
    print("contact not found!")

def save_contacts():
    with open("contacts.csv","w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['city']}\n")

def load_contacts():
    try:
        with open("contacts.csv","r") as file:
            for line in file:
                line=line.strip()
                parts=line.split(",")
                contacts.append({
                    "name":parts[0],
                    "phone":parts[1],
                    "city":parts[2]
                })
    except FileNotFoundError:
        pass            
load_contacts()

while True:
    print("\n---contact book---")
    print("1.Add contact")
    print("2.view contacts")
    print("3.search contacts")
    print("4.delete contacts")
    print("5.Save and Exist")

    while True:
        try:
            choice=int(input("enter a choice:"))
            if choice<1 or choice>5:
                print("Please enter between 1 and 5")
                continue
            break
        except ValueError:
            print("please enter a number")

    if choice==1:
        add_contacts()
    elif choice==2:
        view_contacts()
    elif choice==3:
        search_contact()
    elif choice==4:
        delete_contact()
    elif choice==5:
        save_contacts()
        print("File is saved, goodbye")    
        break
    else:
        print("invalid choice!")                