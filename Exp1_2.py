import math

def sphere_volume(radius):
    """
    Computes the volume of a sphere.
    
    :param radius: Radius of the sphere (float)
    :return: Volume of the sphere (float)
    """
    volume = (4/3) * math.pi * (radius ** 3)
    return round(volume, 2)  # Round off to 2 decimal places

# Example usage
radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"Volume of the sphere: {volume} cubic units")
