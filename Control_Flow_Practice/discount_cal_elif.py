# calculate a discount based on the purchase amount
purchase_amount = 1200  # directly using the amount instead of asking for input
if purchase_amount >= 1000:
    discount = 0.10  # 10% discount
elif purchase_amount >= 500:
    discount = 0.05  # 5% discount
else:
    discount = 0.0  # no discount
final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))