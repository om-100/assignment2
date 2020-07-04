""" Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]"""
def find_sum(numbers):
    n = len(numbers)

    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if numbers[i]+numbers[j]+numbers[k] == 0:
                    print(numbers[i], numbers[j], numbers[k])


numbers = [1, 1, 4, -4, 0, -2, ]
find_sum(numbers)