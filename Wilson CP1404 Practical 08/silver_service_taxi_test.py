from silver_service_taxis import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)

taxi_1 = SilverServiceTaxi("Taxi 1", 100, 2)
taxi_1.drive(18)
print(taxi_1)
print(taxi_1.calculate())