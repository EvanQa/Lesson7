import random
from calendar import MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
from random import choice

#
# for _ in range(10):
#     print(random.randint(a = 10, b = 12), end = " ")
#
# first way
# num1: int = random.randint(a = 0, b = 100)
# num2: int = random.randint(a = 0, b = 100)
# print(f"first  number is {num1}")
# print(f"second  number is {num2}")
# sum_num: int = (num1 + num2)
# answer: int = int(input(f"{num1} + {num2} ="))
# if answer != sum_num:
#     print("you're wrong")
# else:
#     print("you're correct")
#
#
# #second way with while
# num1: int = random.randint(a = 0, b = 100)
# num2: int = random.randint(a = 0, b = 100)
# print(f"first  number is {num1}")
# print(f"second  number is {num2}")
# sum_num: int = (num1 + num2)
# answer: int = int(input(f"{num1} + {num2} ="))
# while answer != sum_num:
#     print("you're wrong")
#     answer: int = int(input(f"{num1} + {num2} ="))
# else:
#     print("you're correct")
#
# choice: int = random.randint(1,2)
# if choice == 1:
#     print(True)
# else:
#     print(False)

print("random day of week: ", random.choice( ["MONDAY","TUESDAY","WEDNESDAY", "THURSDAY","FRIDAY","SATURDAY", "SUNDAY"]))
