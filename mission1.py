def get_expense(prompt):
    return float(input(prompt))

print("Let's See How Much You Spend!")

name = input("What is your name? ")
print(f"Nice to meet you, {name}!")

income = float(input("What is your monthly income? $"))

if income <= 0:
    print("Income must be greater than zero.")
    exit()

print(f"You make ${income:,.2f} per month. Let's calculate your bills to see what remains!")

rent = get_expense("How much do you pay for rent monthly? $")
utilities = get_expense("How much do you pay for utilities monthly? $")
food = get_expense("How much do you budget for food each month? $")
gas = get_expense("How much do you spend on gas each month? $")

subscriptions = get_expense("How much do you pay for subscriptions? $")
debt = get_expense("Any additional debt that you would like to include? $")
insurance = get_expense("How much do you pay for insurance? $")

savings = get_expense("How much would like you like to save each month? $")

calculate_bills = rent + utilities + food + gas
balance = income - calculate_bills
percent = calculate_bills / income

print("")
print("\n=======================")
print(f"{name}'s Monthly Budget Summary")
print("=======================\n")
print("")
print(f"Income:      ${income:,.2f}")
print("")
print(f"Rent:        ${rent:,.2f}")
print(f"Utilities:   ${utilities:,.2f}")
print(f"Food:        ${food:,.2f}")
print(f"Gas:         ${gas:,.2f}")

print("\n=======================\n")

print(f"Total Bills:  ${calculate_bills:,.2f}")
print("")
print(f"Remaining:    ${balance:,.2f}")
print("")
print(f"Income Used: {percent:.1%}")
print("")
if percent < 0.5:
    print(f"Excellent {name}! You're saving a healthy portion of your income!")
elif percent <= 0.7:
    print(f"Not Bad {name}! Keep an eye on discretionary spending!")
else: 
    print(f"YOU SPEND SOME MONEEYYY {name}!! Your Expenses are Consuming your Income!")