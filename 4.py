# question number 4
"""
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""
om = ('om', 'sapkota', 24)
ram_b = ('ram', 'bahadur', 35)
ram = ('Ram', 'Prasad', 26)

people = []

people.append(om)
people.append(ram_b)
people.append(ram)

final = sorted(people)

print(final)