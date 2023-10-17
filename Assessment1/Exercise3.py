# Function to classify the type of triangle
def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

# Prompt user for side lengths
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if it forms a triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("These sides form a triangle.")
    triangle_type = classify_triangle(side1, side2, side3)
    print(f"This is an {triangle_type} triangle.")
else:
    print("These sides do not form a triangle.")
