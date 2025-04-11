class Loan:
    def __init__(self, name, balance, interest_rate, min_payment):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_payment = min_payment

def dynamic_payment_method(loans, budget):
    """Dynamically allocates payments to maximize interest savings while ensuring minimum payments are met."""
    month = 0
    total_interest = 0

    while any(loan.balance > 0 for loan in loans):
        month += 1
        print(f"\nMonth {month} - Dynamic Payment Strategy")

        # Filter out paid-off loans and sort remaining ones by highest interest rate
        active_loans = [loan for loan in loans if loan.balance > 0]
        active_loans.sort(key=lambda loan: loan.interest_rate, reverse=True)

        if not active_loans:
            break

        # Ensure minimum payments can be covered
        total_minimum_payment = sum(loan.min_payment for loan in active_loans)
        if total_minimum_payment > budget:
            print("🚨 Warning: Budget is too low to cover minimum payments!")
            return

        # Allocate remaining budget dynamically
        remaining_budget = budget
        for loan in active_loans:
            # Calculate interest for the month
            monthly_interest = (loan.interest_rate / 100 / 12) * loan.balance
            loan.balance += monthly_interest
            total_interest += monthly_interest

            # Deduct minimum payment first
            payment = min(loan.min_payment, loan.balance)
            loan.balance -= payment
            remaining_budget -= payment

        # If there's extra money, apply dynamically
        if remaining_budget > 0:
            if len(active_loans) > 1:
                # Allocate 60% to highest interest loan, 40% to second highest
                high_priority_loan = active_loans[0]
                secondary_loan = active_loans[1]

                high_priority_payment = min(high_priority_loan.balance, remaining_budget * 0.6)
                secondary_payment = min(secondary_loan.balance, remaining_budget * 0.4)

                high_priority_loan.balance -= high_priority_payment
                secondary_loan.balance -= secondary_payment

                remaining_budget -= (high_priority_payment + secondary_payment)
            else:
                # If only one loan remains, put all remaining budget into it
                active_loans[0].balance -= min(remaining_budget, active_loans[0].balance)

        # Print loan statuses
        for loan in loans:
            print(f"{loan.name}: ${loan.balance:.2f}")

    print(f"\nAll loans paid off in {month} months using Dynamic Payment!")
    print(f"Total interest paid: ${total_interest:.2f}")
    return total_interest

# Example loans
loans = [
    Loan("Car Loan", 5000, 3.5, 200),
    Loan("Credit Card", 7000, 18.0, 150),
    Loan("Student Loan", 10000, 5.0, 300),
]

# Run the method with a fixed budget
dynamic_payment_method(loans, 1000)
