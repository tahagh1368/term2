from pics import HANGMANPICS, words
from random import choice
from string import ascii_lowercase

alphabet = list(ascii_lowercase)
alphabet.append(' ')
answer = choice(words)
guess = list(len(answer)*"?")
i = 0
while i<7:
    print(''.join(guess))
    letter = input("Enter a letter: ").lower()
    while letter not in alphabet:
        letter = input("Enter a letter: ").lower()
    if letter not in answer:
        print(HANGMANPICS[i])
        i = i+1
    else:
        index=-1
        while True:
            try:
                index = answer.index(letter, index+1)
                guess[index] = letter 
            except:
                break
        if ''.join(guess)==answer:
            print(f"Nice. Answer was {answer}")
            break
if i==7:
    print(f"You lost. Answer was {answer}")
    

