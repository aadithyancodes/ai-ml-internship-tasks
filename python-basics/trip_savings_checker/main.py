print("##########################")
print("## TRIP SAVINGS CHECKER ##")
print("##########################")
ticket = float(input("Enter your ticket price (per person): "))
hotel = float(input("Enter the hotel price(per night): "))
nights = int(input("How many nights are you planning to stay? : "))
savings = float(input("Enter your Total Savings: "))
cost = ticket + (hotel*nights)
if savings >= cost+200:
    print("Status: Pack your bags! you have enough money.")
else:
    print("Status: Keep saving. You are short by $",(cost-savings)+200)