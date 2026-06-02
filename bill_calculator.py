price_item1 = float(input("Enter the price of frist item"))
price_item2 = float(input("Enter the price of second item"))
price_item3 = float(input("Enter the price of thrid item"))
actual_amount = price_item1 +  price_item2 + price_item3

if actual_amount > 1000:
   discount_amount = 0.1 * actual_amount
   final_amount = actual_amount - discount_amount

elif actual_amount > 500:
    discount_amount = 0.05 * actual_amount
    final_amount = actual_amount - discount_amount

else:
    discount_amount = 0 * actual_amount
    final_amount = actual_amount - discount_amount

print("Amount before discount" , actual_amount)
print("Discount given" , discount_amount)
print("Amount be to paid", final_amount)