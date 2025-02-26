def triangle_type(a, b, c):
    """
    Determines the type of a triangle based on its side lengths.
    
    :param a: Length of the first side (float)
    :param b: Length of the second side (float)
    :param c: Length of the third side (float)
    :return: Type of triangle (str)
    """
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# Example usage
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

triangle = triangle_type(side1, side2, side3)
print(f"The triangle is: {triangle}")
