print("WELCOME TO SAVINGS PLANNER")

while True:
    balance = float(input("Starting balance: "))
    if balance >= 0:
        break
    print("Balance cannot be negative.")

while True:
    deposit = float(input("Monthly deposit: "))
    if deposit > 0:
        break
    print("Deposit must be positive.")

while True:
    rate = float(input("Monthly interest rate (%): "))
    if rate >= 0:
        break
    print("Interest rate cannot be negative.")

while True:
    goal = float(input("Savings goal: "))
    if goal > 0:
        break
    print("Goal must be positive.")

month = 0
total_interest = 0

print("\nMonth | Interest | Balance")
print("--------------------------")

if balance >= goal:
    print("You already reached your goal!")
else:
    while month < 60:
        month = month + 1

        interest = balance * rate / 100
        balance = balance + interest + deposit
        total_interest = total_interest + interest

        print(f"{month:5} | {interest:8.2f} | {balance:8.2f}")

        if balance >= goal:
            break

print("\nRESULT")

if balance >= goal:
    print("Goal reached in", month, "months.")
else:
    print("Goal not reached after 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest: {total_interest:.2f}")
