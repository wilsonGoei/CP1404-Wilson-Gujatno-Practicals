import random

START_POP = 1000
BIRTH_MIN = 0.1
BIRTH_MAX = 0.2
DEATH_MIN = 0.05
DEATH_MAX = 0.25
def birth():
    percentage = random.uniform(BIRTH_MIN,BIRTH_MAX)
    births = round(percentage,3)*START_POP
    return births

def death():
    percentage = random.uniform(DEATH_MIN,DEATH_MAX)
    deaths = round(percentage,3)*START_POP
    return deaths

def count_total(population,born,died):
    total = population + born - died
    return total

def main():
    print("Welcome to the Gopher Population Simulator!")
    print("Starting Population: {}".format(START_POP))
    print("Year 1\n")
    num = 3
    born = birth()
    died = death()
    population = START_POP + born - died
    print("{:,.0f} gophers were born. {:,.0f} died.".format(born,died))
    print("Population: {:,.0f}".format(population))
    print("Year 2\n")
    for i in range(8):
        born = birth()
        died = death()
        total = count_total(population,born,died)
        print("{:,.0f} gophers were born. {:,.0f} died.".format(born,died))
        print("Population: {:,.0f}".format(total))
        print("Year {}\n".format(num))
        num += 1


main()