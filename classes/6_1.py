# u = input("", "Enter username:")
# if u=='teacher' or u=='student':
#     print('welcome')
# else:
#     print('wrong username or password')

u = input("Enter username: ")
p = input("Enter password: ")
if (u=='teacher' and p=='123') or (u=='student' and p=='poulstar1'):
    print('welcome')
else:
    print('wrong username or password')
