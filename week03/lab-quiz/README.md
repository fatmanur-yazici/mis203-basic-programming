# Week 3 Lab Quiz

I tested the program with an order amount of 500 TRY, available stock of 10,
requested quantity of 2, and member status yes.

The program approved the order and applied the 10% member discount.

After testing, I changed the discount condition from > 500 to >= 500
because an order of exactly 500 TRY should also receive the discount.



## Boundary Tests

| Order Amount | Stock | Requested Quantity | Member | Expected Result |
|---|---|---|---|---|
| 499 TRY | 10 | 2 | yes | Approved, no discount |
| 500 TRY | 10 | 2 | yes | Approved, 10% discount |
| 501 TRY | 10 | 2 | yes | Approved, 10% discount |
