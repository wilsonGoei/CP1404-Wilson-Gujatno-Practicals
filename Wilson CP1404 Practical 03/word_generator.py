"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou#"
CONSONANTS = "bcdfghjklmnpqrstvwxyz%"
format = ["c","v"]

def is_valid_format(format):
    for i in format:
        if i == "c" or i == "v":
            return True
        else:
            return False
        

def main():
    format_input = str(input("Please input the appropriate word [(C)onsonant and (V)owels]: ")).lower()
    while not is_valid_format(format_input):
        print("Invalid input")
        format_input = str(input("Please input the appropriate word [(C)onsonant and (V)owels]: ")).lower()
    word = ""
    for kind in format_input:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    if word == "%re#l":
        print(greatly)
    else:
        print(word)

main()