# 04/07/20
# Evan Johanns
# Palindrome Check
x = int(input("""What would you like to do?
1. Enter Palindrome.
2. Exit.
>> """))
while x != 2:

    def check_palindrome(string):
        if len(string) < 1:
            return True
        elif string[0] == string[-1]:
            return check_palindrome(string[1:-1])
        else:
            return False

    My_string = (str(input("Please enter a Palindrome: ")))
    My_string.strip()
    My_string.lower()
    if check_palindrome(My_string) is True:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome.")
