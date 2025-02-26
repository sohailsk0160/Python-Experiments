# Define a decorator to log function execution
def log_execution(func):
    def wrapper(n):
        print(f"Calculating factorial of {n}...")
        result = func(n)  # Call the original factorial function
        print(f"Factorial of {n} is {result}")
        return result
    return wrapper

# Apply the decorator to the factorial function
@log_execution
def factorial(n):
    """Calculates factorial of a number recursively."""
    return 1 if n == 0 else n * factorial(n - 1)

# Get user input
num = int(input("Enter a number: "))

# Call the decorated function
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial(num)
