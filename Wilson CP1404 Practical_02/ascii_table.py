"""
CP1404/CP5632 - Practical
Ascii Table
"""

LOWER=33
UPPER=127

char=str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(char,ord(char)))
num=int(input("Enter a number between {} and {}: ".format(LOWER,UPPER)))
while num<LOWER or num>UPPER:
    print("Invalid number")
    num = int(input("Enter a number between {} and {}: ".format(LOWER,UPPER)))
print("The character for {} is {}".format(num,chr(num)))

for i in range(LOWER,UPPER+1):
    print("{:10}{:>5}".format(i,chr(i)))