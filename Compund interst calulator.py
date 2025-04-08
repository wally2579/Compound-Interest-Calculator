def compound_interest(principal, rate, times_compounded_per_year, years):
    """
    Calculate the compound interest.
    
    Parameters:
    principal (float): The initial amount of money.
    rate (float): Annual interest rate as a decimal.
    times_compounded_per_year (int): Number of times interest is compounded per year.
    years (int): Time in years the money is invested for.
    
    Returns:
    float: The total amount after compound interest.
    """
    A = principal * (1 + rate / times_compounded_per_year) ** (times_compounded_per_year * years)
    return A

# Example usage
principal = 2000       # Initial amount of money
rate = 0.10            # Annual interest rate (5%)
times_compounded_per_year = 4  # Compounded quarterly
years = 3              # Time in years

final_amount = compound_interest(principal, rate, times_compounded_per_year, years)
print(f"The total amount after {years} years with compound interest is: ${final_amount:.2f}")