letter = input("Enter letter: ").lower()
vowels = "aeiou"

for single in letter:

    if single in vowels:
        print(f"{single} is a vowel")
    else:
        print(f"{single} is a consonant")
