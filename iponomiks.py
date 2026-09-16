
print("=" * 50)
print("            WELCOME TO IPONOMIKS")
print("      Student Expense Tracker")
print("=" * 50)


budget = 0

while True:
    budget_input = input("\nEnter your budget for this month (PHP): ")
    try:
        budget = float(budget_input)
        if budget <= 0:
            print("Budget must be greater than 0. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"\nBudget set to P{budget:,.2f}")


expenses = []          
total_spent = 0

categories = ["Food", "Transportation", "Bills", "School Supplies", "Others"]

running = True

while running:
    print("\n" + "-" * 50)
    print("MAIN MENU")
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. View Budget Summary")
    print("4. Exit")
    print("-" * 50)

    choice = input("Enter your choice (1-4): ").strip()


    if choice == "1":
        print("\nChoose a category:")
        for i in range(len(categories)):
            print(f"  {i + 1}. {categories[i]}")

        while True:
            cat_choice = input("Enter category number: ").strip()
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
                break
            print("Invalid category. Please choose a number from the list.")

        category = categories[int(cat_choice) - 1]

        description = input("Enter a short description: ").strip()
        if description == "":
            description = "(no description)"

        while True:
            amount_input = input("Enter amount spent (PHP): ").strip()
            try:
                amount = float(amount_input)
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        expenses.append((category, description, amount))
        total_spent += amount
        remaining = budget - total_spent

        print(f"\nExpense added: {category} - {description} - P{amount:,.2f}")

        if remaining < 0:
            print(f"WARNING: You are over budget by P{abs(remaining):,.2f}!")
        elif remaining < budget * 0.1:
            print(f"CAUTION: Only P{remaining:,.2f} left of your budget!")
        else:
            print(f"Remaining budget: P{remaining:,.2f}")


    elif choice == "2":
        print("\n" + "-" * 50)
        print("ALL EXPENSES")
        print("-" * 50)

        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            for index in range(len(expenses)):
                exp_category, exp_description, exp_amount = expenses[index]
                print(f"{index + 1}. [{exp_category}] {exp_description} - P{exp_amount:,.2f}")


    elif choice == "3":
        remaining = budget - total_spent
        percent_used = (total_spent / budget) * 100 if budget > 0 else 0

        print("\n" + "-" * 50)
        print("BUDGET SUMMARY")
        print("-" * 50)
        print(f"Total Budget:   P{budget:,.2f}")
        print(f"Total Spent:    P{total_spent:,.2f}")
        print(f"Remaining:      P{remaining:,.2f}")
        print(f"Budget Used:    {percent_used:.1f}%")

        if remaining < 0:
            print("Status: OVER BUDGET")
        elif percent_used >= 90:
            print("Status: NEARLY OVER BUDGET")
        else:
            print("Status: ON TRACK")

  
    elif choice == "4":
        print("\nThank you for using IPONOMIKS. Goodbye!")
        running = False


    else:
        print("Invalid choice. Please enter a number from 1 to 4.")