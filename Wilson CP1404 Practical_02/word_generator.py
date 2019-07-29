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


word_format = ""
for i in range(5):
    word_format += random.choice(format)

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

if word == "%re#l":
    print(greatly)
else:
    print(word)
