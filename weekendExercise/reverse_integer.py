number = int(input("enter any digit number to be reversed: "))

reversed_number = ""

for digit in str(number):
    reversed_number = digit + reversed_number
    convert = int(reversed_number)
print(convert, end="")
