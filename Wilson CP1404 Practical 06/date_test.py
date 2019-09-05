from date import Date

def main():
    day = int(input("Please input the date: "))
    month = int(input("Please input number of month: "))
    year = int(input("Please input number of year: "))
    date = Date(day,month,year)
    print(date)

    add_date = int(input("Enter number to add on the date: "))
    date.add_days(add_date)
    print(date)



main()