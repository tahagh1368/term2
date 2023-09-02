password = 'ali77765'
f = open('note.txt', 'r')
for i in range(100):
    guess = f.readline().strip()
    if guess==password:
        print(f"password is {guess}")
        exit()
print("Cant find password")
