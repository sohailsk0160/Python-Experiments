import math  # Import math module for π (pi)

class Circle:
    def __init__(self, radius):
        """
        Initializes the Circle with a given radius.
        :param radius: Radius of the circle
        """
        self.radius = radius  # Store the radius

    def compute_area(self):
        """
        Computes the area of the circle.
        :return: Area (π * r²)
        """
        return math.pi * self.radius ** 2  # Formula: πr²

    def compute_perimeter(self):
        """
        Computes the perimeter (circumference) of the circle.
        :return: Perimeter (2 * π * r)
        """
        return 2 * math.pi * self.radius  # Formula: 2πr

# Get user input for radius
radius = float(input("Enter the radius of the circle: "))

# Create a Circle object
circle = Circle(radius)

# Print the computed area and perimeter
print(f"Area of the circle: {circle.compute_area():.2f}")
print(f"Perimeter of the circle: {circle.compute_perimeter():.2f}")
