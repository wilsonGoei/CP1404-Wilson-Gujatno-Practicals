def main():
    numbers = []

    print("Please input 5 numbers")
    for i in range(5):
        num = int(input("Number: "))
        numbers.append(num)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

main()