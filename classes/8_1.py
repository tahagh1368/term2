fruits = {
    'apple': 55000,
    'banana': 65000,
    'onion': 15000,
}
fruits.update({'watermelone': 8000})
fruits['watermelone'] = 8000

# a = input("Enter fruit: ")
# print(f"Price of {a} is {fruits.get(a, 'error')}")
# print(fruits.get('apple'))
# print(fruits['apple'])
# items()
# for fruit, price in fruits.items():
#     print(f"Gheymate {fruit} {price} ast.")
# for fruit in fruits.keys():
#     print(fruit)
for a in fruits.values():
    print(a)

