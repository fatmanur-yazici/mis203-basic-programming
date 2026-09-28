# Getting item details and fees from the user
first_item_name = input("Enter First Item Name: ")
first_item_quantity = float(input("Enter First Item Quantity: "))
first_item_price = float(input("Enter First Item Price: "))

second_item_name = input("Enter Second Item Name: ")
second_item_quantity = float(input("Enter Second Item Quantity: "))
second_item_price = float(input("Enter Second Item Price: "))

delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage: "))

# Individual item totals
first_item_total = first_item_quantity * first_item_price
second_item_total = second_item_quantity * second_item_price

# Subtotal (sum of all item totals)
subtotal = first_item_total + second_item_total

# Tax calculation
tax = (subtotal * tax_percentage) / 100

# Final total (Subtotal + Tax + Delivery Fee)
final_total = subtotal + tax + delivery_fee

# Printing the results
print("\n--- ORDER SUMMARY ---")
print(f"Item 1 ({first_item_name}): {first_item_quantity} x {first_item_price} = {first_item_total}")
print(f"Item 2 ({second_item_name}): {second_item_quantity} x {second_item_price} = {second_item_total}")
print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Delivery Fee: {delivery_fee}")
print(f"Final Total: {final_total}")

print("\n--- Purchase Quote ---")
print(f"{first_item_name}: {first_item_total:.2f}TRY")
print(f"{second_item_name}: {second_item_total:.2f}TRY")
print(f"Subtotal: {subtotal:.2f}TRY")
print(f"Tax: {tax:.2f}TRY")
print(f"Delivery: {delivery_fee:.2f}TRY")
print(f"Final total: {final_total:.2f}TRY")
