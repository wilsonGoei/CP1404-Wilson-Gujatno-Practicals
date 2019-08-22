names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

DATES_OF_BIRTH = {}

counter = 0
for name in names:
    DATES_OF_BIRTH [name] = dates_of_birth [counter]
    counter += 1

print(DATES_OF_BIRTH)