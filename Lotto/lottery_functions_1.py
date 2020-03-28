import random
import lottery_tickets



# Prints five random tickets
def main():
    #lottery_tickets.main()
    print(lottery_tickets.main())
    #print(list1[1].random_sampling())
    # call_number()


def shuffle_numbers():
    lottery_nums = list(range(1, 91))
    random.shuffle(lottery_nums)
    return lottery_nums


def call_number():
    count = 0
    numbers = shuffle_numbers()
    return numbers


# def ticket_check():
#     count = 0
#     called_number = call_number()
#     for num in called_number


main()

'''
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

'''
