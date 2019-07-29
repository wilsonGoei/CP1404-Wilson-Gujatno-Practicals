"""
CP1404/CP5632 - Practical
Automatic Password Generator
"""

import random

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
CHARACTERS = "aeioubcdfghjklmnpqrstvwxyz"
NUMBERS = "123456789"

def main():
    length=int(input("Please enter the length of your password: "))
    upper=int(input("Please enter how many uppercase do you want: "))
    lower=int(input("Please enter how many lowercase do you want: "))
    num=int(input("Please enter how many number do you want: "))
    special=int(input("Please enter how many special character do you want: "))
    password = pass_generator(upper,lower,num,special)
    print("Your password with {} length is: {}".format(length,password))

def pass_generator(upper,lower,num,special):
    password = ""
    for i in range(upper):
        password += random.choice(CHARACTERS.upper())
    for x in range(lower):
        password += random.choice(CHARACTERS.lower())
    for y in range(num):
        password += random.choice(NUMBERS)
    for z in range(special):
        password += random.choice(SPECIAL_CHARACTERS)
    pass_list = list(password)
    random.shuffle(pass_list)
    combine_pass = "".join(pass_list)

    return combine_pass






main()