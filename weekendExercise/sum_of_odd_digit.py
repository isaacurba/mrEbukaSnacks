digit = int(input("Enter number to get the sum of the odd digit: "))

sum_of_odd_digit = 0

for number in range(0, digit +1):
    if number % 2 != 0:
        sum_of_odd_digit += number

print(sum_of_odd_digit)
