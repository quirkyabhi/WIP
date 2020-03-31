#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
# import import_ipynb
import lottery_tickets_updated as lottery_tickets


def main():

    # all the tickets created in lottery_ticket
    tickets=lottery_tickets.main()

    # names of each tickets
    Ticket_names = ['Ticket1', 'Ticket2', 'Ticket3', 'Ticket4', 'Ticket5']

    # creating a dictionary of tickets with names of tickets
    myDict1=dict(zip(Ticket_names, tickets))
     
    # Printing the dictionary with name and values
    for name, ticket in myDict1.items():
        ticket.sort()
        print(f"{name} = {ticket}")

    ticket_checking(tickets)


def shuffle_numbers():
    bag_of_numbers = list(range(1, 91))
    random.shuffle(bag_of_numbers)
#     print(bag_of_numbers)
    return bag_of_numbers


def ticket_checking(tickets):
    
    count= 0
    pass1 = True
    pass2 = True
    pass3 = True
    pass4 = True
    pass5 = True
    popper = shuffle_numbers()
    print(popper)
        
    for nums in popper:
        print("the num called is", nums)
        count += 1
        if nums in tickets[0]:
            print(f"Ticket1 has {nums}")
        if nums in tickets[1]:
            print(f"Ticket2 has {nums}")
        if nums in tickets[2]:
            print(f"Ticket3 has {nums}")
        if nums in tickets[3]:
            print(f"Ticket4 has {nums}")
        if nums in tickets[4]:
            print(f"Ticket5 has {nums}")

        for elements in tickets:
            while nums in elements:
                elements.pop(elements.index(nums))

        if not tickets[0]:
            pass1 = False
            break

        if not tickets[1]:
            pass2 = False
            break

        if not tickets[2]:
            pass3 = False
            break

        if not tickets[3]:
            pass4 = False
            break

        if not tickets[4]:
            pass5 = False
            break

    if not pass1:
        print(f"\nAll the numbers in were found in {count} counts")
        print("Ticket1 has won")

    if not pass2:
        print(f"\nAll the numbers in Ticket2 were found in {count} counts")
        print("Ticket2 has won")

    if not pass3:
        print(f"\nAll the numbers in  were found in {count} counts")
        print("Ticket3 has won")

    if not pass4:
        print(f"\nAll the numbers in Ticket4 were found in {count} counts")
        print("Ticket4 has won")

    if not pass5:
        print(f"\nAll the numbers in Ticket5 were found in {count} counts")
        print("Ticket5 has won")

main()

