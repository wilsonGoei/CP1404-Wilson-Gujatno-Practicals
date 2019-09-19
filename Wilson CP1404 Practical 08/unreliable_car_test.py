from unreliable_car import UnreliableCar

car_1 = UnreliableCar("Prius_1", 100, 90)
car_2 = UnreliableCar("Prius_2", 100, 9)

for i in range(1,10):
    print("Attempt {}".format(i))
    print("{} drove {}km".format(car_1.name, car_1.drive(i)))
    print("{} drove {}km".format(car_2.name, car_2.drive(i)))

print(car_1)
print(car_2)