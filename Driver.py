# 04/07/20
# Modded palindrome check
# Evan Johanns
from pal_check import check_palindrome, remove_punct


x = 0
while x != 2:
    x = int(input("""Please type the number of the action you want to perform: 
    1. check palindrome.
    2. exit.
    >> """))

    if x == 1:
        palindrome = str(input("Please enter a palindrome: "))
        palindrome.strip()
        palindrome.lower()
        newLine = str(remove_punct(palindrome))
        if check_palindrome(newLine) is True:
            print("This is NOT a palindrome.")
        else:
            print("This is a palindrome!")
