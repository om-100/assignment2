"""Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors."""

def calc(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == "/":
        try:
            return a/b
        except:
            return 'Cannot divide by 0'
    else:
        return 'Invalid Operator'


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
op = input("Enter the operation to perform: ")
print(calc(a, b, op))