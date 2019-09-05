from guitar import Guitar

def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name,year,cost)
        guitars.append(add_guitar)
        print(add_guitar," added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars: ")
        for index, guitar in enumerate(guitars,1):
            is_vintage = "(vintage)" if guitar.is_vintage() else ""
            print("Guitar {0}: {1.name:>10} ({1.year}), worth ${1.cost:10,.2f} {2}".format(index, guitar, is_vintage))

    else:
        print("No guitars :( Quick, go and buy one!")

main()