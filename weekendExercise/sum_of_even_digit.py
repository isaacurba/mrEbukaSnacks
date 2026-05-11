digit = int(input("Enter number to get the sum of the even digit: "))

sum_of_even_digit = 0

for number in range(0, digit +1):
    if number % 2 == 0:
        sum_of_even_digit += number

print(sum_of_even_digit)
