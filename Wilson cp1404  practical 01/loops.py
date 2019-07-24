""""Loops"""
#displays all of the odd numbers between 1 and 20 with a space between each one
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#print n stars. Ask the user for a number, then print that many stars (*), all on one line
number=int(input("Please input the number of star you want to appear: "))
while number<0:
    print("Invalid number")
    number = int(input("Please input the number of star you want to appear: "))

for i in range(number):
    print("*", end=' ')
print()

#print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1. E.g. if 4 was the number entered, your single loop should print
numbers=int(input("Please input the number of star you want to appear: "))
while numbers<0:
    print("Invalid number")
    numbers = int(input("Please input the number of star you want to appear: "))
for i in range(numbers):
    print("*"*i)
print()


#Add a loop to the sales bonus exercise you did above, so that the program repeatedly asks for the user's sales and prints the bonus until they enter a negative number. Remember that until is the opposite of while.
sales = float(input("Enter sales: $"))

while sales>= 0:
    if sales < 1000:
        bonus = sales * 0.1
        print(bonus)
        sales = float(input("Enter sales: $"))
    else:
        bonus = sales * 0.15
        print(bonus)
        sales = float(input("Enter sales: $"))