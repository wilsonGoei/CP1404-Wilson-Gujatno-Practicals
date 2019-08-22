TARIFF = {11:0.244618, 31:0.136928, 20:0.259256, 51:0.769217, 90:0.842671}


print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? (11/31/20/51/90): "))
daily_use = float(input("Enter number of billing days: "))
number_of_day = int(input("Enter number of billing days: "))
estimated_bill = TARIFF [tariff]*daily_use*number_of_day

print("Estimated bill: ${:.2f}".format(estimated_bill))