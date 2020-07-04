"""Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age."""

def find_average(lists):

    length = len(lists)
    sum = 0

    for tuples in lists:
        if tuples[2] == None:
            pass
        else:
            sum = sum + tuples[2]

    avg = sum/length
    print("Average age is: ", avg)

    for tuples in lists:
        age_check = ''
        if tuples[2] == None:
            print(tuples[0], "Age Undefined")
        else:
            if tuples[2] > avg:
                age_check = 'Old'
            else:
                age_check = 'Young'
            print(tuples[0], age_check)


lists = [('om', 'sapkota', 11), ('ram', 'bahadur', 25),
         ('hari', 'bahadur', 30), ('m', 'prasad', 34), ('hari', 'sharma', None)]
find_average(lists)