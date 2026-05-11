base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = 1

for count in range(exponent):
    result = result * base

print(result)
