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
principal = float(input("Please enter the principle amount you wish to invest: "))       # Initial amount of money
rate = (float(input("Please enter the interest rate offered to you: ")))/100            # Annual interest rate in persentage (eg:5%)
times_compounded_per_year = float(input("Please enter the the duration of time interest whether it be yearly,semi-annually or quaterly is compunded per year: "))  # Compounded '1 for yearly', '2 for semi annually' or '4 for quarterly'
years = float(input("Please enter the period of time(years) you wish to invest your money for: "))              # Time in years

final_amount = compound_interest(principal, rate, times_compounded_per_year, years)
print(f"The total amount after {years} years with compound interest is: ${final_amount:.2f}")