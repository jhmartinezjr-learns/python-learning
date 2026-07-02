def get_expense(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return amount
            print("Please enter a value of 0 or greater.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    name, income = get_user_info()
    
    expenses = collect_expenses()
    savings = collect_savings()
    
    totals = calculate_totals(income, expenses, savings)
    
    print_summary(name, expenses, savings, totals)

def get_user_info():
    print("Let's See How Much You Spend!")
    print()
    
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")
    print()
    
    income = get_expense("What is your monthly income? $")

    if income <= 0:
        print("Income must be greater than zero.")
        exit()

    print(f"You make ${income:,.2f} per month. Let's calculate your bills to see what remains!")
    print()

    return name, income

def collect_expenses():
    return {
        "Fixed Costs": {
            "Rent": get_expense("How much do you pay for rent monthly? $"),
            "Utilities": get_expense("How much do you pay for utilities monthly? $"),
            "Insurance": get_expense("How much do you pay for insurance? $"),
        },
        
        "Variable Costs": {
            "Food": get_expense("How much do you budget for food each month? $"),
            "Gas": get_expense("How much do you spend on gas each month? $"),
            "Subscriptions": get_expense("How much do you pay for subscriptions? $"),
            "Debt": get_expense("Any additional debt that you would like to include? $"),
        }
    }

def collect_savings():
    return {
        "Emergency Fund": get_expense("How much do you want to save for a rainy day? $"),
        "Vacation": get_expense("How much do you want to save for the next vacation? $"),
        "Investments": get_expense("How much money do you want to invest? $"),
    }

def calculate_totals(income, expenses, savings):
    total_expenses = sum(sum(section.values()) for section in expenses.values())   
    total_savings = sum(savings.values())
    
    remaining_after_expenses = income - total_expenses
    final_remaining = remaining_after_expenses - total_savings

    return {
        "total_expenses": total_expenses,
        "total_savings": total_savings,
        "final_remaining": final_remaining,
        "expense_ratio": total_expenses / income,
        "savings_ratio": total_savings / income,
    }

def print_summary(name, expenses, savings, totals):
    print(f"\n{name}'s Monthly Budget Summary\n")

    for section, items in expenses.items():
        print(section)
        for category, amount in items.items():
            print(f"{category:<20} ${amount:>10,.2f}")

    print("\nSavings")
    for goal, amount in savings.items():
        print(f"{goal:<25} ${amount:,.2f}")

    print("\nTotals")
    print(f"Total Bills:              ${totals['total_expenses']:,.2f}")
    print(f"Planned Savings:          ${totals['total_savings']:,.2f}")
    print(f"Remaining After Savings:  ${totals['final_remaining']:,.2f}")
    print(f"Income Used:               {totals['expense_ratio']:.1%}")
    print(f"Savings Goal:              {totals['savings_ratio']:.1%}")

    if totals["expense_ratio"] < 0.5:
        print(f"Excellent work, {name}! You're using less than half of your income on expenses.")
    elif totals["expense_ratio"] <= 0.7:
        print(f"Good job, {name}. You're spending is under control, but there may be opportunities to save more.")
    elif totals["expense_ratio"] <= .9:
        print(f"Careful, {name}. A large portion of your income is going toward monthly expenses.")
    else: 
        print(f"Warning {name}. Your expenses are consuming nearly all of your income. Consider reviewing your budget.")
        
if __name__ == "__main__":
    main()