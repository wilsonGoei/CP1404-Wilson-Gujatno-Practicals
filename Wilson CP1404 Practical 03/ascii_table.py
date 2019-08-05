"""
CP1404/CP5632 - Practical
Ascii Table
"""

LOWER=33
UPPER=127

def get_number():
    while True:
        try:
            num=int(input("Enter a number between {} and {}: ".format(LOWER,UPPER)))
            if num < LOWER or num > UPPER:
                print("Please enter a valid number")
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    return num



def main():
    char=str(input("Enter a character: "))
    print("The ASCII code for {} is {}".format(char,ord(char)))

    ascii_num = get_number()


    print("The character for {} is {}".format(ascii_num,chr(ascii_num)))

    for i in range(LOWER,UPPER+1):
       print("{:10}{:>5}".format(i,chr(i)))

main()