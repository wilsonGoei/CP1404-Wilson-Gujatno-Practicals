from car_simulator import Car

def main():
    print("Let's drive!")
    name = str(input("Enter your car name: "))
    car = Car(name,100)
    print(car)
    menu = str(input("Menu:\nd)drive\nr)refuel\nq)quit\nEnter your choice: ")).upper()
    while menu != "Q":
        if menu == "D":
            distance = int(input("How many km do you wish to drive?"))
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive?"))
            if car.fuel < distance:
                print("The car drove {}km and ran out of fuel\n".format(car.fuel))
            else:
                print("The car drove {}km\n".format(distance))
            car.drive(distance)
            print(car)
            menu = str(input("Menu:\nd)drive\nr)refuel\nq)quit\nEnter your choice: ")).upper()
        elif menu == "R":
            fuel = int(input("How many units of fuel do you want to add to the car? "))
            while fuel < 0:
                print("Fuel amount must be >= 0")
                fuel = int(input("How many units of fuel do you want to add to the car? "))
            print("Added {} units of fuel.\n".format(fuel))
            car.refuel(fuel)
            print(car)
            menu = str(input("Menu:\nd)drive\nr)refuel\nq)quit\nEnter your choice: ")).upper()
        else:
            print("Invalid choice\n")
            print(car)
            menu = str(input("Menu:\nd)drive\nr)refuel\nq)quit\nEnter your choice: ")).upper()
    print("\nGood bye {}'s driver.".format(name))


main()