import json
import tkinter as tk
from collections import defaultdict
import matplotlib.pyplot as plt

income = []
expense = []


def show_expense_pie():
    expense_cat = defaultdict(float)
    for item in expense:
        expense_cat[item["category"]] += item["amount"]

    labels = list(expense_cat.keys())
    sizes = list(expense_cat.values())
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution by Category")
    plt.show()


def load_data():
    global income, expense
    try:
        with open("finance_data.json", "r") as f:
            data = json.load(f)
            income = data.get("income", [])
            expense = data.get("expense", [])
    except FileNotFoundError:
        income = []
        expense = []


load_data()

root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("400x300")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Category").grid(row=0, column=0, padx=5, pady=5)
entry_category = tk.Entry(frame_input)
entry_category.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Amount").grid(row=1, column=0, padx=5, pady=5)
entry_amount = tk.Entry(frame_input)
entry_amount.grid(row=1, column=1, padx=5, pady=5)


def show_category_summary():
    income_cat = defaultdict(float)
    expense_cat = defaultdict(float)

    for item in income:
        income_cat[item["category"]] += item["amount"]
    for item in expense:
        expense_cat[item["category"]] += item["amount"]
    print("Income by category:", dict(income_cat))
    print("Expense by category: ", dict(expense_cat))


def save_data():
    with open("finance_data.json", "w") as f:
        json.dump({"income": income, "expense": expense}, f)


lbl_message = tk.Label(root, text="", fg="red")
lbl_message.pack(pady=5)


def add_income_ui():
    try:
        category = entry_category.get()
        amount = float(entry_amount.get())
        income.append({"category": category, "amount": amount})
        save_data()

        lbl_message.config(text=f"Added Income: {amount} to {category}")
    except ValueError:
        lbl_message.config(text="Invalid amount. Please enter a number.")


def add_expense_ui():
    try:
        category = entry_category.get()
        amount = float(entry_amount.get())
        expense.append({"category": category, "amount": amount})
        save_data()
        lbl_message.config(text=f"Added Expense: {amount} to {category}")
    except ValueError:
        lbl_message.config(text="Invalid amount. Please enter a number.")


frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Add Income", command=add_income_ui).pack(
    side=tk.LEFT, padx=5
)
tk.Button(frame_buttons, text="Add Expense", command=add_expense_ui).pack(
    side=tk.LEFT, padx=5
)

lbl_summary = tk.Label(root, text="", fg="blue")
lbl_summary.pack(pady=10)


def show_summary_ui():
    total_income = sum(item["amount"] for item in income)
    total_expense = sum(item["amount"] for item in expense)
    balance = total_income - total_expense
    lbl_summary.config(
        text=f"Total Income : {total_income} Total Expense: {total_expense} Balance: {balance}"
    )


tk.Button(frame_buttons, text="Show Summary", command=show_summary_ui).pack(
    side=tk.LEFT, padx=5
)

tk.Button(root, text="Show Expense Pie Chart", command=show_expense_pie).pack(pady=5)
# while True:
#     choice = input(
#         "Add Income (i) / Add Expense (e) /Show Summary (ss) / Quit (q): "
#     ).lower()
#     if choice == "i":
#         add_income()
#     elif choice == "e":
#         add_expense()
#     elif choice == "ss":
#         show_summary()
#         break
#     elif choice == "q":
#         break
#     else:
#         print("Invalid Choice")


# print("Income:" + str(income))
# print("Expense:" + str(expense))
root.mainloop()
