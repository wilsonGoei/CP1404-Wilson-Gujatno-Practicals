from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.5
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * Taxi.price_per_km

    def calculate(self):
        total = (super().get_fare()) + self.flagfall
        return total

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
