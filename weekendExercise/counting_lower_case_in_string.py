word = input("Enter any word to count the upper case in it: ")
count = 0
for char in word:
    if char.islower():
        count += 1

print(count)
