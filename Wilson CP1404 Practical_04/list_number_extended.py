def main():
    numbers = []

    print("Please input 5 numbers")
    counter = 1
    while True:
        num = int(input("Number {}: ".format(counter)))
        if num > 0:
            numbers.append(num)
            counter += 1
        else:
            break
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

main()