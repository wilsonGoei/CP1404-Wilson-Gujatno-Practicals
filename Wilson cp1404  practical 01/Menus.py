"""Use this pattern to create a very simple menu-driven program according to the pseudocode below:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message"""


def main():
    name=str(input("Enter name: "))
    ans=True
    while ans:
        menu=str(input("(H)ello\n(G)oodbye\n(Q)uit\n"))
        choice=menu.upper()
        if choice == "H":
            print("\nHello ", name)

        elif choice == "G":
            print("\nGoodbye ", name)
        elif choice == "Q":
            print("\nFinished")
            ans=None
        else:
            print("\nInvalid choice")





main()