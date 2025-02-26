def sum_natural(n):
    """
    Recursively calculates the sum of the first n natural numbers.
    
    :param n: The number up to which the sum is calculated
    :return: Sum of natural numbers from 1 to n
    """
    if n <= 0:
        return 0  # Base case: Sum of 0 natural numbers is 0
    return n + sum_natural(n - 1)  # Recursive case: n + sum of (n-1)

# Get user input
num = int(input("Enter a number: "))

# Check for valid input
if num < 0:
    print("Please enter a positive integer.")
else:
    result = sum_natural(num)
    print(f"Sum of first {num} natural numbers is: {result}")
