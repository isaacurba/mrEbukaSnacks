word = input("Enter any word to check if its a palindrome: ")
copy = word
reverse = ""

for letter in word:
    reverse = letter + reverse

if reverse == copy:
    print(f"{copy} is a palindrome")
else: print(f"{copy} is not a palindrome")
