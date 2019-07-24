"""" electricity bill estimator 1.0
Inputs should be:

daily use in kWh, and

number of days in the billing period.

Modify your bill estimator by asking the user to choose which tariff they are using - then use the appropriate stored value for cents per kWh.
Start by defining two constants like below.
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
def main():
    print("Electricity bill estimator")
    choice=int(input("Which tariff? 11 or 31: "))
    while choice<11 or 11>choice<31 or choice>31:
        print("Invalid number")
        choice = input("Which tariff? 11 or 31: ")

    if choice == 11:
        tariff=TARIFF_11
    else:
        tariff=TARIFF_31
    daily_use=float(input("Enter daily use in kWh: "))
    billing=float(input("Enter number of billing days: "))
    total=tariff*daily_use*billing
    print("Estimated bill: ${0:.2f}".format(total))
main()