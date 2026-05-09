x = int(input("Enter x integer: "))
y = int(input("Enter y integer: "))

if x > 0 and y > 0:
    print("Q1")
if x < 0 and y > 0:
    print("Q2")
if x < 0 and y < 0:
    print("Q3")
if x > 0 and y < 0:
    print("Q4")
if x == 0 and y == 0:
    print("Origin")
if y == 0 and x != 0:
    print("x-axis")
if x == 0 and y != 0:
    print("y-axis")
