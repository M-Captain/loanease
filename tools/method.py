class Loan:
    def __init__(self, name, balance, interest_rate, min_payment):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_payment = min_payment

def snowball_method(loans, extra_payment):
    loans.sort(key=lambda loan: loan.balance)  # Sort by balance (smallest first)
    return pay_off_loans(loans, extra_payment, method="Snowball")

def avalanche_method(loans, extra_payment):
    loans.sort(key=lambda loan: loan.interest_rate, reverse=True)  # Sort by interest (highest first)
    return pay_off_loans(loans, extra_payment, method="Avalanche")

def pay_off_loans(loans, extra_payment, method):
    """Simulates the loan repayment process."""
    month = 0
    while any(loan.balance > 0 for loan in loans):
        month += 1
        print(f"\nMonth {month} - {method} Method")

        for loan in loans:
            if loan.balance <= 0:
                continue  # Skip paid loans

            # Apply minimum payment
            loan.balance -= loan.min_payment

        # Find the loan to apply extra payment
        for loan in loans:
            if loan.balance > 0:
                payment = min(extra_payment, loan.balance)
                loan.balance -= payment
                extra_payment -= payment
                break  # Apply extra payment to one loan at a time

        for loan in loans:
            print(f"{loan.name}: ${loan.balance:.2f}")

    print(f"\nAll loans paid off in {month} months using the {method} method!")
    return month

loans = [
    Loan("Car Loan", 5000, 3.5, 200),
    Loan("Credit Card", 7000, 18.0, 150),
    Loan("Student Loan", 10000, 5.0, 300),
]
loan = [
    Loan("Car Loan", 5000, 3.5, 200),
    Loan("Credit Card", 7000, 18.0, 150),
    Loan("Student Loan", 10000, 5.0, 300),
]

extra_payment = 500  # Extra amount you want to pay

print("\n--- Using Snowball Method ---")
snowball_method(loans.copy(), extra_payment)

print("\n--- Using Avalanche Method ---")
avalanche_method(loan, extra_payment)
