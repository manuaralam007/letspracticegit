#This function help to find palindrome string

def is_palindrome(s):
    return s == s[::-1]

my_string = "dcbaabcd"
if is_palindrome(my_string):
    print(f"'{my_string}' is a palindrome.")
else:
    print(f"'{my_string}' is not a palindrome")