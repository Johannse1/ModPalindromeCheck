# 04/07/20
# Modded palindrome check
# Evan Johanns
from pal_check import check_palindrome

def remove_punct(string):
    line = string
    newline = ""
    if not line.isalpha():
        for char in line:
            if char.isalpha():
                newline += char
    return newline


x = 0
while x != 2:
    x = int(input("""Please type the number of the action you want to preform: 
    1. check palindrome.
    2. exit.
    >> """))

    if x == 1:
        palindrome = input("Please type your palindrome to be checked: ")
        remove_punct(palindrome)
        check_palindrome(palindrome)


