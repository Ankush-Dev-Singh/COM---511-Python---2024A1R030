# A student records monthly expenses under different categories. Write a program that combines the expenses for each category and reports the total amount spent. Category names are case-insensitive. For example, Food, FOOD, and food represent the same category. Display: 1. The total monthly expense. 2. Each category and its total, ordered from highest to lowest expenditure. 3. The category with the highest expenditure. If two categories have the same expenditure, display them in alphabetical order. If multiple categories tie for the highest expenditure, the alphabetically first category is the highest-spending category reported. Input Format

# The first line contains an integer n, the number of expense entries.
# Each of the next n lines contains a category name and an amount, separated by a space.
# Category names contain no spaces.
n = int(input())

expenses = {}
total = 0

for _ in range(n):
    category, amount = input().split()
    category = category.lower()
    amount = float(amount)

    expenses[category] = expenses.get(category, 0) + amount
    total += amount

# Sort by highest amount, then alphabetically
sorted_expenses = sorted(expenses.items(), key=lambda x: (-x[1], x[0]))

print(f"Total Monthly Expense: {total:.2f}")
print("Expenses by Category:")

for category, amount in sorted_expenses:
    print(f"{category} : {amount:.2f}")

# Highest category
highest_category, highest_amount = sorted_expenses[0]

print(f"Highest Expense Category: {highest_category}")
print(f"Highest Expense Amount: {highest_amount:.2f}")