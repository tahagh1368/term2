def input1(text):
    a = input(text)
    while len(a)!=1:
        a = input(text)
    return a

m = input1("Enter a character: ")
print(m)

