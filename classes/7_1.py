#           0         1         2           3
foods = ['pizza', 'kalbas', 'hamberger', 'soosis']
drinks = ['sprite', 'fanta', 'doogh']
# print(drinks)
# drinks.sort() # محتویات لیست را به طور صعودی مرتب میکند.
# drinks.reverse() # محتویات لیست را برعکس میکند.
# print(drinks)
# a = input(f"What do you want?{foods}")
# if a in foods:
#     i = foods.index(a) # شماره خانه ای از لیست که در آن a هست را تحویل میدهد.
#     t = foods.pop(i) # با دادن شماره خانه، آن آیتم از لیست را به ما تحویل میدهد.
#     print(f"Here you are {t}")
#     print(foods)
# else:
#     print(f"{a} Not in list")
# foods.extend(drinks) # دو لیست را با هم ادغام میکند.
o = input("Enter new food")
foods.append(o) # آیتم مورد نظر را به آخر لیست اضافه میکند.
foods.insert(0,o) # آیتم مورد نظر را به خانه ای از لیست که گفتیم اضافه میکند.
print(foods)