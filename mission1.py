print("Let's See How Much You Spend!")

get_user_name = input("What is your name? ")

print(f"Nice to meet you, {get_user_name}!")

get_income = float(input("What is your monthly income? $"))

if get_income <= 0:
    print("Income must be greater than zero.")
    exit()

print(f"You make ${get_income:,.2f} per month. Let's calculate your bills to see what remains!")

rent = float(input("How much do you pay for rent monthly? $"))
utilities = float(input("How much do you pay for utilities monthly? $"))
food = float(input("How much do you budget for food each month? $"))
gas = float(input("How much do you spend on gas each month? $"))

calculate_bills = rent + utilities + food + gas
balance = get_income - calculate_bills
percent = calculate_bills / get_income

print("")
print("=======================")
print(f"{get_user_name}'s Monthly Budget Summary")
print("=======================")
print("")
print(f"Income:      ${get_income:,.2f}")
print("")
print(f"Rent:        ${rent:,.2f}")
print(f"Utilities:   ${utilities:,.2f}")
print(f"Food:        ${food:,.2f}")
print(f"Gas:         ${gas:,.2f}")
print("")
print("=======================")
print("")
print(f"Total Bills:  ${calculate_bills:,.2f}")
print("")
print(f"Remaining:    ${balance:,.2f}")
print("")
print(f"Income Used: {percent:.1%}")
print("")
if percent < 0.5:
    print(f"Excellent {get_user_name}! You're saving a healthy portion of your income!")
elif percent <= 0.7:
    print(f"Not Bad {get_user_name}! Keep an eye on discretionary spending!")
else: 
    print(f"YOU SPEND SOME MONEEYYY {get_user_name}!! Your Expenses are Consuming your Income!")