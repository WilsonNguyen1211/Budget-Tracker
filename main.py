BUDGET = 0
EXPENSES = {}


def set_budget():  # returns an int
    while True:
        balance = input("What is your budget? ")
        if balance.isdigit():
            balance = float(balance)
            if balance < 0:
                print("Please enter a positive number.")
            else:
                return balance
        else:
            print("Please enter a valid number.")


def get_balance(budget, expenses_dict):
    total_expenses = sum(expenses_dict.values())
    balance = budget - total_expenses
    return balance


def add_expenses(expenses_dict, expense, cost):  # return string
    while True:
        cost = float(cost)
        if cost < 0:
            print("Please enter a positive number.")
        else:
            expenses_dict[expense] = cost
            print("Expenses added successfully!")
            break


def get_expenses(expenses_dict):  # return dictionary
    print("Expenses:")
    for expense_name, cost in expenses_dict.items():
        print(f"{expense_name}: ${cost}")


def remove_expense(expenses_dict, key):  # return string
    if key in expenses_dict:
        del expenses_dict[key]
        return f"Expense '{key}' removed successfully!"
    else:
        return f"Expense '{key}' not found."


def main():
    while True:
        print("Welcome to Budget Tracker")
        print("-------------------------")
        print("1. Set budget\n"
              "2. Get balance\n"
              "3. Add expenses\n"
              "4. Get expenses\n"
              "5. Remove expenses\n"
              "6. Quit\n")
        choice = input("What do you want to do? ")

        if choice == "1":
            BUDGET = set_budget()
            print(f"Your budget is ${BUDGET}\n")
        elif choice == "2":
            balance = get_balance(BUDGET, EXPENSES)
            print(f"Your current balance is ${balance}")
        elif choice == "3":
            expense = input("What is your expense? ")
            cost = input("What is the cost? $")
            add_expenses(EXPENSES, expense, cost)
        elif choice == "4":
            get_expenses(EXPENSES)
        elif choice == "5":
            key_to_remove = input("Enter the expense to remove: ")
            print(remove_expense(EXPENSES, key_to_remove))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
