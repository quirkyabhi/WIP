import random

lottery_nums = list(range(1, 91))

ticket_1 = random.sample(lottery_nums, k=15)
print(f"The winning ticket is: \n{ticket_1[0:5]}\n{ticket_1[5:10]}\n{ticket_1[10:15]}")

print("")

ticket_2 = random.sample(lottery_nums, k=15)
print(f"The winning ticket is: \n{ticket_2[0:5]}\n{ticket_2[5:10]}\n{ticket_2[10:15]}")

print("")

# randomly choosing a number from the list and removing the number from the main list
count = 0
while True:
    random.shuffle(lottery_nums)
    pop1 = lottery_nums.pop(0)
    print(" The number called is", pop1)
    count += 1
    if pop1 in ticket_1:
        match = ticket_1.pop(ticket_1.index(pop1))
        print("Yayyy")
    else:
        print("Bad Luck")
    if not ticket_1:
        break
    if not lottery_nums:
        break

print(f"All the numbers in ticket1 were found in {count} counts")
#print(f"All the numbers in the {ticket_1} were found in {count} counts")


# IN SETS THE POSITION DOES NOT MATTER
# count = 0
# while True:
#     lottery_call = random.sample(lottery_nums, k=15)
#     set_lottery_call = set(lottery_call)
#     print(f"\n{lottery_call[0:5]}\n{lottery_call[5:10]}\n{lottery_call[10:15]}")
#     win_set = set(ticket_1)
#     count += 1
#     if set_lottery_call == win_set:
#         print("The lottery matches after:", count)
#         break
