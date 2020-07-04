# question number 2
def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year, "it is a leap year")
    elif year % 400 == 0:
        print(year, "it is a leap year")
    else:
        print("not a leap year ")
year = int(input("enter a year: "))
leap(year)

