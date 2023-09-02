# sentence = """Hello my name appel is Mohammad fallah. Good luck."""
# print(sentence)
# # sentence = sentence.lower() # همه را به حروف کوچک تبدیل میکند.
# # sentence = sentence.upper() # همه را به حروف بزرگ تبدیل میکند.
# # sentence = sentence.capitalize() # همه حروف را کوچک میکند. حرف اول جمله را بزرگ میکند..
# # sentence = sentence.title() # حرف اول تمام کلمات را بزرگ میکند..
# # sentence = sentence.count('a') # تعداد کاراکتر خواسته شده را میشمارد.
# # sentence = sentence.split('.') # بر اساس کاراکتری که تعیین کردیم متن را تکه تکه میکند.
# sentence = sentence.find('my') # اندیس جایی که کاراکتر مورد نظر پیدا شد را به ما تحویل میدهد.
# # sentence = sentence.replace('appel', 'apple') # در کل جمله کاراکتر اولی را با دومی جایگزین میکند.
# # sentence.strip() # اسپیس و اینتر های اضافه اول و آخر متن را حذف میکند.

# print(sentence)

# print(len(['ali' , 'reza', 'omid']))
# name = list('mohammad')
# name[1]='t'
# print(name)

# from string import ascii_lowercase, digits
# for i in ascii_lowercase + digits:
#     for j in ascii_lowercase + digits:
#         for k in ascii_lowercase + digits:
#             for t in ascii_lowercase + digits:
#                 print(f'{i}{j}{k}{t}')

try:
    answer = ['e', 'l', 'e', 'p', 'h', 'a', 'n', 't', 'e', 'e', 'a', 'b', 'e']
    i = answer.index('e',13)
    print(i)
except:
    pass

