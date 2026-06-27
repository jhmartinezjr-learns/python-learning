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

expenses = [
    rent,
    utilities,
    food,
    gas,
    subscriptions,
    debt,
    insurance,
]

total_expenses = sum(expenses)

remaining_after_expenses = income - total_expenses
final_remaining = remaining_after_expenses - savings

expense_ratio = total_expenses / income
savings_ratio = savings / income

print("")
print("\n=======================")
print(f"{name}'s Monthly Budget Summary")
print("=======================\n")

print(f"Income:                   ${income:,.2f}")
print("\n=======================")
print("Fixed Costs")
print("=======================\n")
print(f"Rent:                     ${rent:,.2f}")
print(f"Utilities:                ${utilities:,.2f}")
print(f"Food:                     ${food:,.2f}")
print(f"Gas:                      ${gas:,.2f}")
print(f"Insurance:                ${insurance:,.2f}")

print("\n=======================")
print("Variable Costs")
print("=======================\n")
print(f"Subscriptions:            ${subscriptions:,.2f}")
print(f"Debt:                     ${debt:,.2f}")


print("\n=======================")
print("Totals")
print("=======================\n")

print(f"Total Bills:              ${total_expenses:,.2f}")
print("")
print(f"Planned Savings:          ${savings:,.2f}")
print("")
print(f"Remaining After Savings:  ${final_remaining:,.2f}")
print("")
print(f"Income Used:               {expense_ratio:.1%}")
print("")
print(f"Savings Goal:              {savings_ratio:.1%}")
print("")

if expense_ratio < 0.5:
    print(f"Excellent work, {name}! You're using less than half than half of your income on expenses.")
elif expense_ratio <= 0.7:
    print(f"Good job, {name}. You're spending is under control, but there may be opportunities to save more.")
elif expense_ratio <= .9:
    print(f"Careful, {name}. A large portion of your income is going toward monthly expenses.")
else: 
    print(f"Warning {name}. Your expenses are consuming nearly all of your income. Consider reviewing your budget.")