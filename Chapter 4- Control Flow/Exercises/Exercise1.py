# Define the initial color of the alien
alien_color = 'green'

# Check if the alien's color is green
if alien_color == 'green':
    # If the color is green, print a message and award 5 points
    print("You just earned 5 points!")

# Change the alien's color to red
alien_color = 'red'

# Check if the alien's color is green (this check will fail because the color is now red)
if alien_color == 'green':
    # This code block will not execute because the color is not green
    print("You just earned 5 points!")    
