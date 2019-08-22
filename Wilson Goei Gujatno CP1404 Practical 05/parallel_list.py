DATES_OF_BIRTH = {}

for i in range(3):
    name = str(input("Name: "))
    dob = str(input("Date of Birth (dd/mm/yyyy): "))
    day, month, year = dob.split("/")
    DATES_OF_BIRTH [name] = day, month, year

for key,value in DATES_OF_BIRTH.items():
    values = list(value)
    age = 2019 - int(values[2])
    print(key, age)