# Create a list of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'veggie', 'turkey']

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders and make each sandwich
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)  # Move the made sandwich to finished sandwiches

# Print a message listing each sandwich that was made
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
