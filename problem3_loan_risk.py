# Loan risk classification

credit_score = int(input("Enter the credit score: "))
annual_income = float(input("Enter the annual income: "))

# Classify the applicant using the required risk rules.
if credit_score >= 720 and annual_income >= 60000:
    risk_category = "Low Risk"
elif credit_score >= 650 and annual_income >= 40000:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

print(f"Loan Risk Category: {risk_category}")
