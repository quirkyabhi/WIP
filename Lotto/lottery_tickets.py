import random


class Lottery:

    def __init__(self):
        self.lottery_nums = list(range(1, 91))

    def random_sampling(self):
        return random.sample(self.lottery_nums, k=15)


def main():
    list1 = []
    no_of_tickets = 5
    for num in range(no_of_tickets):
        tickets = Lottery()
        tickets.random_sampling()
        list1.append(tickets)
        return list1


# @staticmethod
#     def multiple_tickets():
#         no_of_tickets = 5
#         for tickets in range(no_of_tickets):
#             tickets = Lottery()
#             print(f"Ticket is: \n{tickets.random_sampling()[0:5]}"
#                   f"\n{tickets.random_sampling()[5:10]}"
#                   f"\n{tickets.random_sampling()[10:15]}")
#
# Lottery.multiple_tickets()
