def compute_future_value(principal, rate, years):
    """
    Computes the future value of an investment.
    
    :param principal: Initial amount of money invested (float)
    :param rate: Annual interest rate (as a percentage, e.g., 5 for 5%)
    :param years: Number of years the money is invested (int)
    :return: Future value of the investment (float)
    """
    # Convert rate to decimal
    rate = rate / 100  

    # Compute future value
    future_value = principal * (1 + rate) ** years  

    return round(future_value, 2)  # Round off to 2 decimal places

# Example usage
principal_amount = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))

future_value = compute_future_value(principal_amount, annual_rate, years)
print(f"Future Value: {future_value}")
