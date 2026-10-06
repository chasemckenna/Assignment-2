# Employee performance bonus calculation

annual_salary = float(input("Enter the annual salary: "))
performance_score = float(input("Enter the performance score (0-100): "))

# Determine the bonus percentage based on the performance score.
if performance_score >= 90:
    bonus_percentage = 20
elif performance_score >= 80:
    bonus_percentage = 10
elif performance_score >= 70:
    bonus_percentage = 5
else:
    bonus_percentage = 0

bonus_amount = annual_salary * bonus_percentage / 100

print(f"Performance Bonus: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount:,.2f}")
