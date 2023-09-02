from asc import *
from random import choice
from time import sleep

def save():
    f = open("ascii_art_game.txt", 'w')
    for food in foods:
        f.write(food)
        f.write('\n')
    f.write('\n')
    for food in macrofer_foods:
        f.write(food)
        f.write('\n')
    f.close()

def random_item(items):
    return choice(items)

def get_input(items):
    item = input(items)
    while item not in items:
        print("Not in item list. choose again: ")
        item = input(items)
    return item

def show_place(item):
    if item == 'sleep':
        for i in range(5, 0, -1):
            sleep(1)
            print("Sleeping!!!")
        show_place('room')
    elif item=='exit':
        exit()
    elif item in foods and item not in ['kitchen', 'exit']:
        print(names[item])
        foods.remove(item)
        sleep(1)
        save()
        show_place('kitchen')
    elif item in macrofer_foods and item not in ['kitchen', 'exit']:
        t = int(input("Enter seconds: "))
        for i in range(t, 0, -1):
            print(i)
            sleep(1)
        print(names[item])
        macrofer_foods.remove(item)
        sleep(2)
        save()
        show_place('kitchen')
    print(names[item])
    item = get_input(actions[item])
    show_place(item)

try:
    f = open("ascii_art_game.txt", 'r')
    foods = []
    while True:
        line = f.readline().strip()
        if line == "":
            break
        foods.append(line)
    macrofer_foods = []
    while True:
        line = f.readline().strip()
        if line == "":
            break
        macrofer_foods.append(line)
except:
    foods = ['kitchen', 'apple', 'egg', 'chocolate','icecream', 'cheese', 'drink', 'cake', 'exit']
    macrofer_foods = ['kitchen', 'pizza', 'exit']

names = {
    'room': room,
    'kitchen': kitchen,
    'house': salon,
    'salon': salon,
    'tv': remote,
    'exit': exit,
    'out': out,
    'remote': tv_off,
    'tv1': tv1,
    'tv2': tv2,
    'tv3': tv3,
    'tv4': tv4,
    'tv_off': tv_off,
    'fridge': Refrigerator,
    'apple': apple,
    'drink': drink,
    'chocolate': chocolate,
    'cake': cake,
    'cheese': cheese,
    'egg': egg,
    'icecream': icecream,
    'macrofer': macrofer,
    'pizza': pizza
}
actions = {
    'room': ['sleep', 'lamp', 'salon', 'exit'],
    'kitchen': ['salon', 'macrofer', 'fridge','exit'],
    'house': ['room', 'kitchen', 'tv', 'exit'],
    'salon': ['room', 'kitchen', 'tv', 'exit'],
    'tv': ['salon', 'remote', 'exit'],
    'out': ['house', 'exit'],
    'remote': ['tv1', 'tv2', 'tv3', 'tv4', 'exit', 'salon'],
    'tv1': ['tv2', 'tv3', 'tv4', 'tv_off', 'exit', 'salon'],
    'tv2': ['tv1', 'tv3', 'tv4', 'tv_off', 'exit', 'salon'],
    'tv3': ['tv1', 'tv2', 'tv4', 'tv_off', 'exit', 'salon'],
    'tv4': ['tv1', 'tv2', 'tv3', 'tv_off', 'exit', 'salon'],
    'tv_off': ['tv1', 'tv2', 'tv3', 'tv4', 'exit', 'salon'],
    'fridge': foods,
    'macrofer': macrofer_foods,
}

show_place('out')
