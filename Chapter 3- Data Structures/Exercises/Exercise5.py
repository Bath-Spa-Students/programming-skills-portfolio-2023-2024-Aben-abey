# Define the initial list of guests
guests = ['Alice', 'Bob', 'Charlie', 'David']

# Print the original list of guests
print("Original list of guests:")
for guest in guests:
    print(guest)

# Print a message saying one guest can't make it
print("\nUnfortunately, Charlie can't make it to dinner.")

# Replace Charlie with a new guest
guests[2] = 'Eve'

# Print a message stating the guest who can't make it
print("\nUpdate: Charlie can't make it to dinner. Eve is invited instead.")

# Print a second set of invitation messages
print("\nSecond set of invitation messages:")
for guest in guests:
    print(f"{guest}, you're invited to dinner.")


