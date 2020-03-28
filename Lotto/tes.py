import random


class Lottery:

    def __init__(self):
        self.lottery_nums = list(range(1, 91))

    def random_sampling(self):
        return random.sample(self.lottery_nums, k=15)

    def three_layer_list(self):
        return (f"\n{Lottery.random_sampling(self)[0:5]}"
              f"\n{Lottery.random_sampling(self)[5:10]}"
              f"\n{Lottery.random_sampling(self)[10:15]}")

def main():
    list1 = []
    no_of_tickets = 5
    for num in range(no_of_tickets):
        tickets = Lottery()
        tickets.random_sampling()
        list1.append(tickets)
    print(list1[0].random_sampling())
    print(list1[1].random_sampling())

main()