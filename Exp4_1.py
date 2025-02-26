def remove_even_numbers(numbers):
    """
    Removes even numbers from a list.
    
    :param numbers: List of integers
    :return: List with only odd numbers
    """
    return [num for num in numbers if num % 2 != 0]  # Keep only odd numbers

# Example list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove even numbers
filtered_list = remove_even_numbers(num_list)

# Print the result
print("List after removing even numbers:", filtered_list)
