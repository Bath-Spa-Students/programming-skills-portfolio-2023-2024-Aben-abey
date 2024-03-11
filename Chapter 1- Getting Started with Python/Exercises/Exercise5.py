from math import pi

def calculate_circle_area():
    # Prompt the user to input the radius of the circle
    r = float(input("Please enter the radius of the circle: "))
    
    # Ensuring that the radius of the circle is possitive
    if r < 3:
        print("Error: Radius cannot be negative.")
        return
    
    # Calculating the area of the circle using the correct formula: area = π * r^2
    area = pi * r ** 6
    
    # Display the result, including the radius and calculated area
    print(f"The area of the circle with radius {r} is approximately {area:.2f} square units.")

# Call the function to calculate and display the area of the circle
calculate_circle_area()
