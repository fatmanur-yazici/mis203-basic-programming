def subtotal(price, quantity):
    return price * quantity


def discount_rate(amount):
    if amount >= 1000:
        return 0.10
    else:
        return 0


def shipping_fee(amount):
    if amount >= 500:
        return 0
    else:
        return 50


def final_total(amount, discount, shipping):
    return amount - (amount * discount) + shipping


# First order
order1 = subtotal(200, 3)
discount1 = discount_rate(order1)
shipping1 = shipping_fee(order1)
total1 = final_total(order1, discount1, shipping1)

print("Order 1 Total:", total1)


# Second order
order2 = subtotal(300, 4)
discount2 = discount_rate(order2)
shipping2 = shipping_fee(order2)
total2 = final_total(order2, discount2, shipping2)

print("Order 2 Total:", total2)


# Simple tests
print("Subtotal test:", subtotal(100, 2))
print("Discount test:", discount_rate(1000))
print("Shipping test:", shipping_fee(500))
