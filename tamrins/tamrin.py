name = input("Name khod ra vared konid: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
age = int(age)
# age = int(input("Enter your age: "))
print("Welcome", name, surname, ". You are", age, "years old.",
"You will be", age+1, "next year.")
print(f"Welcome {name} {surname}. You are {age} \
    years old. You will be {age+1} next year.")
