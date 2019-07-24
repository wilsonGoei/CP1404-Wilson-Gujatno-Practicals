"""" electricity bill estimator 1.0
Inputs should be:

price per kWh in cents,

daily use in kWh, and

number of days in the billing period."""

def main():
    print("Electricity bill estimator")
    numbers=float(input("Enter cents per kWh: "))
    cents=numbers/100
    daily_use=float(input("Enter daily use in kWh: "))
    billing=float(input("Enter number of billing days: "))
    total=cents*daily_use*billing
    print("Estimated bill: ",total)
main()