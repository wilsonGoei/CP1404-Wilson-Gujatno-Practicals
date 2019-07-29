"""
CP1404/CP5632 - Practical
Ascii Column Challenge
"""

LOWER=33
UPPER=127
MIN_COLUMNS=1
MAX_COLUMNS=10

columns=int(input("Please input number of columns you want to print (number is between {} and {}): ".format(MIN_COLUMNS,MAX_COLUMNS)))

while columns < MIN_COLUMNS or columns > MAX_COLUMNS:
    print("Invalid input, please choose another number")
    columns = int(input("Please input number of columns you want to print (number is between {} and {}): ".format(MIN_COLUMNS,MAX_COLUMNS)))

data=UPPER - LOWER + 1
rows=data//columns

count = LOWER
for i in range(rows):
    for x in range(columns):
        print("{:10} {:>5}".format(count,chr(count)),end=" ")
        count += 1
    print()

first_counter = count
for count in range(first_counter,UPPER+1):
    print("{:10} {:>5}".format(count,chr(count)),end=" ")
print()