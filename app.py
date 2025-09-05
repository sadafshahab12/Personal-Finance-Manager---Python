income = []
expense = []


def add_income():
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    income.append({"category": category, "amount": amount})
    print("Income added successfully.")


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expense.append({"category": category, "amount": amount})
    print("Expense added successfully.")


def show_summary():
    total_income = sum(item["amount"] for item in income)
    total_expense = sum(item["amount"] for item in expense)
    balance = total_income - total_expense
    print(f"Total Income: {balance}")


while True:
    choice = input(
        "Add Income (i) / Add Expense (e) /Show Summary (ss) / Quit (q): "
    ).lower()
    if choice == "i":
        add_income()
    elif choice == "e":
        add_expense()
    elif choice == "ss":
        show_summary()
        break
    elif choice == "q":
        break
    else:
        print("Invalid Choice")


print("Income:" + str(income))
print("Expense:" + str(expense))
