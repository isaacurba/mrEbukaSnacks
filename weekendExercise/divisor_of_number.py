number = int(input("Enter number: "))

print(f"The numbers that can divide {number} are")
for divisor in range(1, number):
    if number % divisor == 0:
        print(divisor)
