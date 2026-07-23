expenses = []

num_expenses = int(input("How many expenses do you want to enter? "))

for i in range(num_expenses):
    description = input("What did you spend on? ")

    try:
        amount = float(input("How much did you spend? $"))
    except ValueError:
        print("That's not a valid number. Setting this expense to $0.")
        amount = 0

    expense = {"description": description, "amount": amount}
    expenses.append(expense)

print("\nHere's everything you entered:")
for expense in expenses:
    print(f"- {expense['description']}: ${expense['amount']}")
total_spent = 0
for expense in expenses:
    total_spent = total_spent + expense['amount']

print(f"\nTotal spent: ${total_spent:.2f}")

budget = float(input("What's your budget? $"))

if total_spent > budget:
    over_by = total_spent - budget
    print(f"You're over budget by ${over_by:.2f}!")
elif total_spent == budget:
    print("You spent exactly your budget. Cutting it close!")
else:
    remaining = budget - total_spent
    print(f"You're under budget! You have ${remaining:.2f} left.")