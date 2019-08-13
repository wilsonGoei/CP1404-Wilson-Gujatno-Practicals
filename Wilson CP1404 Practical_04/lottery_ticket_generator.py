import random

NUMBERS = []

def random_number():
    random_numbers = []
    for x in range(6):
        rand_num = random.randint(1,45)
        if rand_num in NUMBERS:
            rand_num = random.randint(1, 45)
            NUMBERS.append(rand_num)
        NUMBERS.append(rand_num)
        random_numbers.append(rand_num)

    random_numbers.sort()
    return random_numbers

def main():
    how_many = int(input("How many quick picks? "))
    while how_many < 0:
        print("Invalid input")
        how_many = int(input("How many quick picks? "))

    list_number = []
    for i in range(how_many):
        random_num = random_number()
        list_number.append(random_num)

    for j in range(len(list_number)):
        print(*list_number[j], sep=" ")

main()