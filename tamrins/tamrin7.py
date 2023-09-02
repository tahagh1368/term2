from pics import HANGMANPICS, words
from random import choice
from string import ascii_lowercase

answer = choice(words)
guess = list(len(answer)*"?")
i = 0
while i<7:
    print(''.join(guess))
    letter = input("Enter a letter: ").lower()
    while letter not in list(ascii_lowercase):
        letter = input("Enter a letter: ").lower()
    if letter != answer:
        print(HANGMANPICS[i])
        i = i+1
    else:
        print(f"Nice. Answer was {answer}")
        break

if i==7:
    print(f"You lost. Answer was {answer}")
    