# f = open('note.txt', 'w') # write
# f.write('hello\n')
# f.close()
# f = open('note.txt', 'a') # append
# f.write('bye\n')
# f.close()
f = open('note.txt', 'r') # read
# data = f.read()
# data = f.readlines()
for i in range(5):
    data = f.readline().strip()
    print(data)
f.close()

