# Define the list of places to visit
places_to_visit = ['Japan', 'Italy', 'Australia', 'Brazil', 'Canada']

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Print the list in its original order again
print("Original order after sorting:", places_to_visit)

# Print the list in reverse alphabetical order using sorted() with reverse=True
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Print the list in its original order again
print("Original order after reverse sorting:", places_to_visit)

# Reverse the order of the list using reverse()
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Reverse the order of the list again to get back to the original order
places_to_visit.reverse()
print("Original order after double reversing:", places_to_visit)

# Sort the list in alphabetical order using sort()
places_to_visit.sort()
print("Alphabetical order after sorting:", places_to_visit)

# Sort the list in reverse alphabetical order using sort() with reverse=True
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order after sorting:", places_to_visit)
