# Customer discount eligibility

purchase_amount = float(input("Enter the purchase amount: "))
membership_status = input("Are you a member? (yes/no): ").strip().lower()

# Apply the membership and purchase amount rules.
if membership_status == "yes":
    if purchase_amount >= 100:
        discount_percentage = 15
    else:
        discount_percentage = 5
else:
    if purchase_amount >= 150:
        discount_percentage = 10
    else:
        discount_percentage = 0

final_price = purchase_amount * (1 - discount_percentage / 100)

print(f"Discount applied: {discount_percentage}%")
print(f"Final price: ${final_price:.2f}")
