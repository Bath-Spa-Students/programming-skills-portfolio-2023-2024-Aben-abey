while True:
    try:
        age = int(input("Enter your age (or 'quit' to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue
    
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    if age == 'quit':
        break