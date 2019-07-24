"""A school teacher requires a small program that would allow primary school students to learn about various number sequences. The teacher is interested in a simple menu-driven program that has the following choices (where x and y are inputs the user enters once at the start of the program):

Show the even numbers from x to y

Show the odd numbers from x to y

Show the squares from x to y

Exit the program"""

def main():
    ans=True
    while ans:
        menu=str(input("\ni. Show the even numbers from x to y \nii. Show the off numbers from x to y \niii.Show the squares from x to y \niv.Exit the program \n"))
        choice=menu.lower()
        if choice == "i" or choice == "1":
            x=int(input("Please input the first number: "))
            y=int(input("Please input the second number: "))
            for i in range(x,y+1):
                if i % 2 == 0:
                    print(i, end=" ")
        elif choice == "ii" or choice == "2":
            x=int(input("Please input the first number: "))
            y=int(input("Please input the second number: "))
            for i in range(x,y+1):
                if i % 2 != 0:
                    print(i, end=" ")
        elif choice == "iii" or choice == "3":
            x=int(input("Please input the first number: "))
            y=int(input("Please input the second number: "))
            for i in range(x,y+1):
                print(i**2, end=" ")
        elif choice =="iv" or choice == "4":
            print("Goodbye")
            ans=None
        else:
            print("Invalid choice")

main()