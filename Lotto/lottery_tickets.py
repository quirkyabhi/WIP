import random

class Lottery:

    def __init__(self):
        self.lottery_nums = list(range(1, 91))

    def random_sampling(self):
        return random.sample(self.lottery_nums, k=15)

def main():
    no_of_tickets = 5
    list1 = []
    tickets = [Lottery().random_sampling() for i in range(no_of_tickets)]
    for ticket in tickets:
        list1.append(ticket)
    return list1

# main()
# print(main())


