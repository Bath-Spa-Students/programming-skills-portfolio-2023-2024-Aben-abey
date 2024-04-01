# Define the initial list of guests
guests = ['Alice', 'Bob', 'Charlie', 'David']

# Print a message saying only two people can be invited
print("Sorry, we can only invite two people for dinner.")

# Remove guests from the list one by one until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to the two people still on the list
for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

# Remove the last two names from the list using del
del guests[1:]
print(guests)  # Print the empty list to verify
