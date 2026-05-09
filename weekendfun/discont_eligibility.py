# Use float for height to allow decimals like 1.75
total_bill = int(input("Enter your total bill: "))
is_member = input("are you a member of the community (yes / no): ")


if total_bill >= 1000 and is_member == "yes":
    print("10% off")
elif total_bill >= 1000 and is_member == "no":
    print("5% off")
else:
    print(f"your total bill is ${total_bill} you have no discount")
