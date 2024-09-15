# tries = 0
# num: int = 0
# while num != 777:
#     num: int = int(input("enter number"))
#     tries += 1
#     if num == 0:
#         print("num is 0")
#         break
# else:
#     print(f"well done!, in {tries} tries")
grades_sum: int = 0

for _ in range(3):
    x: int = int(input("enter the grade"))
    if x < 0:
        print("wrong grade")
        break
    grades_sum += x
else:
    grades_sum = grades_sum // 3
    print(f"the sum of u grades are: {grades_sum}")


