math_questions = {
    '4**3=?': [17, 64, 16, 256, 1],
    '6*3=?': [17, 64, 18, 256, 2]
}
math_questions = {
    '4**3=?': {
        'a1': 16,
        'a2': 20,
        'a3': 98,
        'a4': 64,
        'answer': 64
    },
    '6*3=?': {
        'a1': 17,
        'a2': 64,
        'a3': 18,
        'a4': 256,
        'answer':18
    }
}
print('4**3=?')
print(math_questions['4**3=?']['a1'])
print(math_questions['4**3=?']['a2'])
print(math_questions['4**3=?']['a3'])
print(math_questions['4**3=?']['a4'])
k = int(input("Enter correct answer: "))
if k == math_questions['4**3=?']['answer']:
    print("Right")
elif k in [math_questions['4**3=?']['a1'], math_questions['4**3=?']['a2'], math_questions['4**3=?']['a3']]:
    print("Wrong")
else:
    print("jumped this question")