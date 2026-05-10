student_fail = 0
student_pass = 0
score = 0

for number in range(1, 16):
    score = int(input(f"Enter student {number} score: "))
    if score > 45:
        student_pass += 1
    elif score < 45:
        student_fail += 1

print(f"{student_pass} student passed")
print(f"{student_fail} student failed")
