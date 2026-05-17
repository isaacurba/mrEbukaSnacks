import random

def random_subtraction_number():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, first_number)
    return first_number, second_number
