""""A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen."""
prices = []

def main():
    item=int(input("Number of items: "))

    for i in range(item):
        price = float(input("Price of item: "))
        while price < 0:
            print("Invalid number")
            price = float(input("Price of item: "))
        prices.append(price)
    print("Total price for ",item," is: $",sum(prices))


main()