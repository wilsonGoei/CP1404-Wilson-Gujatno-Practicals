"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180,"my car")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


    limo = Car(100, "limo")
    limo.add_fuel(20)
    print("\nfuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)

    print("\n{}".format(my_car))

    name = str(input("\nPlease input your car name: "))
    car =Car(180,name)
    print(car)
main()