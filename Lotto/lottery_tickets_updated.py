#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class Lottery:

    def __init__(self):
        self.lottery_nums = list(range(1, 91))

    def random_sampling(self):
        return random.sample(self.lottery_nums, k=15)

def main():
    no_of_tickets = 5
    tickets = [Lottery().random_sampling() for i in range(no_of_tickets)]
    return tickets

