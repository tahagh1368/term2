contacts = {}
name = ''
while name != 'end':
    name = input("Enter name: ")
    if name=='end':
        break
    if name in contacts:
        print(f"{name}'s number is {contacts.get(name)}")
    else:
        answer = input("Do you want to add? (y/n)")
        # while answer not in ['y', 'n']:
        #     answer = input("Do you want to add? (y/n)")
        if answer in ['yes', 'y', 'are', 'ok', 'bale']:
            number = input("Enter number: ")
            contacts[name]=number
f = open('contacts.txt', 'w')
f.write(str(contacts))
print("End of program.")