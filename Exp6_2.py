def fibonacci_recursive(n):
    """
    Generates the Fibonacci series up to n terms using recursion.
    
    :param n: Number of terms
    :return: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_recursive(n - 1)  # Recursive call
        series.append(series[-1] + series[-2])  # Add next term
        return series

# Get user input
num = int(input("Enter the number of terms: "))

# Print Fibonacci series
print("Fibonacci Series (Recursive):", fibonacci_recursive(num))
