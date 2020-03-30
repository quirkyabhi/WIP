numbers = [[21, 32], [32, 67], [56, 22], [89, 78], [5, 90]]
Ticket_names = ['Ticket1', 'Ticket2', 'Ticket3', 'Ticket4', 'Ticket5']
myDict1 = dict()
value1 = 0
for ele in Ticket_names:
    myDict1.setdefault(ele, numbers[value1])
    value1 += 1

print(myDict1)

nums = 32
if nums in numbers[0]:
    print("Ticket1 has a match")
if nums in numbers[1]:
    print("Ticket2 has a match")
for items in numbers:  # items0 = [21, 34]
    while nums in items:
        items.pop(items.index(nums))

print(numbers)



