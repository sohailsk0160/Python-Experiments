def check_element_in_tuple(tup, element):
    """
    Checks if an element is present in the tuple.
    
    :param tup: Tuple of elements
    :param element: Element to check
    :return: True if element is found, otherwise False
    """
    return element in tup  # Returns True if element is found, otherwise False

# Example tuple
my_tuple = (10, 20, 30, 40, 50)

# Get user input
element = int(input("Enter the element to search: "))

# Check if the element is in the tuple
if check_element_in_tuple(my_tuple, element):
    print(f"{element} is present in the tuple.")
else:
    print(f"{element} is NOT present in the tuple.")
