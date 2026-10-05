
order_amount = float(input("Enter order amount: "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
member = input("Is the customer a member? (yes/no): ").lower()

if requested_quantity <= 0:
    print("Order rejected.")
    print("Reason: Invalid requested quantity.")

elif requested_quantity > available_stock:
    print("Order rejected.")
    print("Reason: Insufficient stock.")

else:
    print("Order approved.")
    print("Reason: Valid quantity and enough stock.")

    if member == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Member discount: 10%")
    else:
        final_price = order_amount

    print("Final price:", final_price, "TRY")

