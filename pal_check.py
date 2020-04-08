# 04/07/20
# Evan Johanns
# Palindrome Check


def remove_punct(string): # check for any punctuation and removes all
    line = string
    newLine = ""
    if not line.isalpha():
        for char in line:
            if char.isalpha():
                newLine+=char
    return print(newLine)

def check_palindrome(string):
    if len(string) < 1:
        return True
    elif string[0] == string[-1]:
        return check_palindrome(string[1:-1]) # reverses the string and checks from the beginning, recursion
    else:
        return False
