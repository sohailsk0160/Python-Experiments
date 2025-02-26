def is_prime(n):
    """
    Checks if a number is prime.
    
    :param n: Integer to check
    :return: True if prime, otherwise False
    """
    if n < 2:
        return False  # Prime numbers start from 2

    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  # If divisible, not a prime

    return True  # If no divisors found, it's prime

# Get user input
num = int(input("Enter a number to check if it's prime: "))

# Check and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")
