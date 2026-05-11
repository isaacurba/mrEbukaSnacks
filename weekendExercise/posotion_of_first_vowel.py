word = input("Enter a word: ")
vowels = "aeiouAEIOU"

for index in range(len(word)):
    if word[index] in vowels:
        print(f"The first vowel is at position: {index}")
        break
else:
    print("No vowels found.")
