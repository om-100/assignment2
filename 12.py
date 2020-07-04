"""
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""
def is_palindrome(word):
    rev = word[::-1]
    if word == rev:
        return True
    else:
        return False


word = input("Enter a word: ")
print(is_palindrome(word))