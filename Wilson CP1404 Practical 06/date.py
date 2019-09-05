days_in_month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Date:
    def __init__(self, day, month, year):
        self.day = days_in_month[day]
        self.month = month
        self.year = year

    def add_days(self,amount):
        self.day += amount
        if self.day > 31:
            self.day = 1
            self.month += 1
        elif self.month > 12:
            self.day = 1
            self.month = 1
            self.year += 1

    def __str__(self):
        return "Day = {}\nMonth = {}\nYear = {}\n".format(self.day,month_names[self.month],self.year)