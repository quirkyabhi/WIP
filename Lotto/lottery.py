
# random.choices(Lottery_numbers, k=4) # this would random choose but there would be repetitions

# print(lottery_call)


# Lottery_numbers = [12, 18, 25, 96, 64, 60, 83, 5, 53, 'j', 'a', 't', 'r', 'q']
# lottery_win = [12, 't', 53, 96]
# count = 0

# while True:
#     lottery_call = random.sample(Lottery_numbers, k=4)
#     print(lottery_call)
#     count += 1
#     if len([x for x in lottery_win if x in lottery_call]) == len(lottery_win):
#         print("The lottery matches after:", count)
#         break


# while True:
#     lottery_call = random.sample(Lottery_numbers, k=4)
#     #lottery_call = [12, 25, 64, 5]
#     print(lottery_call)
#     count += 1
#     list = []
#     for elements in lottery_call:
#         if elements in lottery_win:
#             list.append(elements)
#
#     if len(list) == len(lottery_win):
#         print("The lottery matches after:", count)
#         break

import random

Lottery_numbers = [12, 18, 25, 96, 64, 38, 60, 83, 5, 53, 'j', 'a', 't', 'r', 'q']
lottery_win = [12, 't', 53, 96]
count = 0

# IN SETS THE POSITION DOES NOT MATTER
# while True:
#     lottery_call = set(random.sample(Lottery_numbers, k=4))
#     print(list(lottery_call))
#     win_set = set(lottery_win)
#     count += 1
#     if lottery_call == win_set:
#         print("The lottery matches after:", count)
#         break

list = [1, 2, 3, 4, 6, 8, 45, 87, 0]

number = 45
if number in list:
    print(list.index(number))
#match = list.pop()


