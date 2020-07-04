#question number 5
"""
Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""


def sort_people(people):
    om = ('om', 'sapkota', 24)
    john = ('John', 'Doe', 35)
    ram = ('Ram', 'Prasad', 26)

    people = []
    people.extend((om, john, ram))

    people.sort(key=lambda x: x[1])
    return people
people = []
print("Sorted according to Last Name : \n ", sort_people(people))

