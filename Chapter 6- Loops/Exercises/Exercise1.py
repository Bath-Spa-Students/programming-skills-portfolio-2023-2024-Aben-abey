toppings = []  # Initialize an empty list to store toppings

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    toppings.append(topping)  # Add the topping to the list
    print(f"You'll add {topping} to your pizza.")

print("Your pizza toppings:")
for topping in toppings:
    print(topping)
