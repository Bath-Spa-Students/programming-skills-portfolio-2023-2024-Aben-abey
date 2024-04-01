# Create a dictionary of major rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# Print a sentence about each river using a loop
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print()  # Insert a blank line for better readability

# Print the names of each river using a loop
print("Names of rivers:")
for river in rivers.keys():
    print(river)

print()  # Insert a blank line for better readability

# Print the names of each country using a loop
print("Names of countries:")
for country in rivers.values():
    print(country)
