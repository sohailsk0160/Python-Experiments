import math

class Polygon:
    def __init__(self, num_sides):
        """Initializes a polygon with a given number of sides."""
        self.num_sides = num_sides
        self.sides = [0] * num_sides  # Initialize list to store side lengths

    def input_sides(self):
        """Takes input for all sides of the polygon."""
        self.sides = [float(input(f"Enter length of side {i+1}: ")) for i in range(self.num_sides)]

    def display_sides(self):
        """Displays the sides of the polygon."""
        print("Sides of the polygon:", self.sides)

class Triangle(Polygon):
    def __init__(self):
        """Initializes a triangle (inherits from Polygon with 3 sides)."""
        super().__init__(3)  # A triangle has 3 sides

    def compute_area(self):
        """Computes the area of the triangle using Heron's formula."""
        a, b, c = self.sides  # Extract side lengths
        s = (a + b + c) / 2  # Semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
        return area

# Create a Triangle object
triangle = Triangle()

# Input and display the sides
triangle.input_sides()
triangle.display_sides()

# Compute and display the area
print(f"Area of the triangle: {triangle.compute_area():.2f}")
