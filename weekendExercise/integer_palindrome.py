number = int(input("Enter number to check if its a palindrome: "))
copy = number
reverse = ""

for digit in str(number):
    reverse = digit + reverse
    convert = int(reverse)

if convert == copy:
    print(f"{copy} is a palindrome")
else: print(f"{copy} is not a palindrome")
