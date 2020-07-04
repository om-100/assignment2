"""
Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return "Enter number greater than 1"


number = int(input("ENter a number: "))
print(is_prime(number))