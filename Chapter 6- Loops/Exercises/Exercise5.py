# Create a list of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'veggie', 'turkey']

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders and make each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Get the first sandwich order
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)  # Move the made sandwich to finished sandwiches

# Print the list of finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
