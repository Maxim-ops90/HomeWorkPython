# # Реализуйте алгоритм перемешивания списка.


# import random

# def get_list(n, lft, rght):
#     return [random.randint(lft, rght) for i in range(n)]

# def shuffle_list(lst):
#     return random.shuffle(lst)

# n = 20
# lft = -30
# rght = 50

# mylist = get_list(n, lft, rght)
# print(mylist)
# shuffle_list(mylist)
# print(mylist)


import numbers


numbers = [1, 2, 3, 4, 5]
for counter, item in enumerate(numbers):
    if (counter % 2 == 0):
        print(counter)

# print(counter)
