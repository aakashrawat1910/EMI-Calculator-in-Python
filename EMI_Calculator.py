import math

def calculate_emi(principal, rate, duration):
    """
    Calculates the Equated Monthly Installment (EMI) for a loan.
    
    Parameters:
    principal (float): The total loan amount.
    rate (float): The annual interest rate as a percentage (e.g. 10.5 for 10.5%).
    duration (int): The loan duration in years.
    
    Returns:
    float: The calculated EMI amount.
    """
    # Convert annual interest rate to monthly rate
    monthly_rate = rate / (12 * 100)
    
    # Calculate EMI
    emi = principal * monthly_rate * (1 + monthly_rate)**(duration * 12) / ((1 + monthly_rate)**(duration * 12) - 1)
    
    return round(emi, 2)

# Get user input
principal = float(input("Enter the loan principal amount: "))
rate = float(input("Enter the annual interest rate (e.g. 7.5 for 7.5%): "))
duration = int(input("Enter the loan duration in years: "))

emi = calculate_emi(principal, rate, duration)
print(f"The EMI for a loan of {principal:,.2f} at {rate}% interest over {duration} years is {emi:,.2f}")