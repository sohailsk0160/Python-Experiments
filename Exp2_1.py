def find_largest(a, b, c):
    """
    Finds the largest number among three numbers.
    
    :param a: First number (float)
    :param b: Second number (float)
    :param c: Third number (float)
    :return: Largest number (float)
    """
    largest = max(a, b, c)  # Using the built-in max function
    return largest

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest_number = find_largest(num1, num2, num3)
print(f"The largest number is: {largest_number}")
