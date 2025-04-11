from scipy.optimize import linprog

class Loan:
    def __init__(self, name, balance, interest_rate, min_payment):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        self.min_payment = min_payment

def ai_optimized_method(loans, total_budget):
    """Uses linear programming to minimize total interest paid while staying within budget."""
    num_loans = len(loans)

    # Objective function: Minimize interest paid in one month
    interest_rates = [loan.interest_rate / 100 / 12 for loan in loans]  # Monthly interest rates

    # Inequality constraint: sum(payments) <= total_budget
    A_ub = [[1] * num_loans]  # Upper bound constraint
    b_ub = [total_budget]

    # Bounds: Payments must be between minimum payments and loan balances
    bounds = [(loan.min_payment, min(total_budget, loan.balance)) for loan in loans]

    # Solve the optimization problem
    result = linprog(interest_rates, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

    if result.success:
        print("\nOptimized Payments per Loan (AI Model Suggestion):")
        for i, loan in enumerate(loans):
            print(f"{loan.name}: ${result.x[i]:.2f} per month")
    else:
        print("🚨 Optimization failed! Check budget and constraints.")

# Example loans
loans = [
    Loan("Car Loan", 5000, 3.5, 200),
    Loan("Credit Card", 7000, 18.0, 150),
    Loan("Student Loan", 10000, 5.0, 300),
]

# Run AI optimization with a budget of $1000
ai_optimized_method(loans, 1000)
