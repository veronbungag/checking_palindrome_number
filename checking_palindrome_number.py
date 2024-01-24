#define a function for checking palindrome number
def check_palindrome(number):
#check the string is equal to its reverse then its palindrome number
    return str(number) == str(number)[::-1]
#convert number to string then user input number
number = int(input("Enter a number: "))
#check if the user input is palindrome number if it is then print
if check_palindrome(number):
    print(f"{number} is a palindrome number.")
#if not print not a palindrome number
else:
    print(f"{number} is not a palindrome number.")