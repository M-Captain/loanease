# def calculate_emi(principal, annual_interest, tenure_years):
#     monthly_interest = annual_interest / 1200  # Convert annual interest rate to monthly
#     months = tenure_years * 12  # Convert years to months

#     # EMI Formula
#     emi = (principal * monthly_interest * (1 + monthly_interest) ** months) / ((1 + monthly_interest) ** months - 1)
#     emi = round(emi, 2)  # Round to 2 decimal places
#     return emi, monthly_interest

# def generate_emi_schedule(principal, annual_interest, tenure_years, prepayment=0, prepayment_months=[]):
#     emi, monthly_interest = calculate_emi(principal, annual_interest, tenure_years)

#     print(f"\n🎯 Monthly EMI: ₹{emi}")
#     print("===================================================================")
#     print(f"{'Month':<6} {'EMI':<10} {'Principal Paid':<15} {'Interest Paid':<15} {'Remaining Principal'}")
#     print("===================================================================")

#     month = 1
#     while principal > 0:
#         interest_paid = round(principal * monthly_interest, 2)  # Interest for the month
#         principal_paid = round(emi - interest_paid, 2)  # Principal paid
#         principal = round(principal - principal_paid, 2)  # Remaining principal

#         # Apply Prepayment if it's in the prepayment_months list
#         if month in prepayment_months and principal > 0:
#             prepay_amount = min(prepayment, principal)  # Ensure we don't overpay beyond the principal
#             principal -= prepay_amount
#             print(f"🎉 Prepayment of ₹{prepay_amount} made in month {month}")

#         print(f"{month:<6} ₹{emi:<10} ₹{principal_paid:<15} ₹{interest_paid:<15} ₹{principal}")

#         # Stop when the principal is fully paid
#         if principal <= 0:
#             print("\n🎉 Loan fully paid off earlier due to prepayment! 🚀")
#             break

#         month += 1

# # User Input
# principal = float(input("Enter Loan Amount: "))
# annual_interest = float(input("Enter Annual Interest Rate (%): "))
# tenure_years = int(input("Enter Loan Tenure (in years): "))
# prepayment = float(input("Enter Prepayment Amount (₹): "))
# prepayment_months = list(map(int, input("Enter Prepayment Months (comma-separated, e.g., 6,12,18): ").split(',')))

# generate_emi_schedule(principal, annual_interest, tenure_years, prepayment, prepayment_months)
