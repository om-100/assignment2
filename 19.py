"""Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid"""
def is_valid(strings):
    stack = []
    dictonary = {"(": ")", "{": "}", "[": "]"}

    for item in strings:
        if item in dictonary:
            stack.append(item)

        elif dictonary[stack.pop()] != item:
            return False

    return len(stack) == 0  #return False if any one paranthesis remains un popped


print(is_valid("(){[]}"))
print(is_valid("({)}"))