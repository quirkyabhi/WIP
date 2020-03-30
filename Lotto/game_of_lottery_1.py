import random
import lottery_tickets

def main():

    # all the tickets created in lottery_tickets
    tickets = [lottery_tickets.main()[0], lottery_tickets.main()[1],
               lottery_tickets.main()[2], lottery_tickets.main()[3],
               lottery_tickets.main()[4]]

    # names of each tickets
    Ticket_names = ['Ticket1', 'Ticket2', 'Ticket3', 'Ticket4', 'Ticket5']

    # creating a dictionary of tickets with names of tickets
    myDict1 = dict()
    value1 = 0

    for ele in Ticket_names:
        myDict1.setdefault(ele, tickets[value1])
        value1 += 1

    # Printing the dictionary with name and values
    for name, ticket in myDict1.items():
        ticket.sort()
        print(f"{name} = {ticket}")

    ticket_checking(tickets)


def shuffle_numbers():
    bag_of_numbers = list(range(1, 91))
    list_numbers = []
    while True:
        random.shuffle(bag_of_numbers)
        pop1 = bag_of_numbers.pop(0)
        list_numbers.append(pop1)
        if not bag_of_numbers:
            break
    return list_numbers


def ticket_checking(tickets):
    count = 0
    pass1 = True
    pass2 = True
    pass3 = True
    pass4 = True
    pass5 = True
    popper = shuffle_numbers()
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