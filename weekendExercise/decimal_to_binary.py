decimal = int(input("Enter decimal number to convert to binary: "))

binary_result = ""

while decimal > 0:
    last_digit = decimal % 2
    binary_result = str(last_digit) + binary_result
    decimal = decimal // 2

print(binary_result)
