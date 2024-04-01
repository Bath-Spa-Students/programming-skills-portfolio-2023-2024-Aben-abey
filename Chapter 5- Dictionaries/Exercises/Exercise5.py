pets = [
    {
        'animal': 'dog',
        'owner': 'John Doe'
    },
    {
        'animal': 'cat',
        'owner': 'Jane Smith'
    },
    {
        'animal': 'bird',
        'owner': 'Mike Johnson'
    }
]

# print the information about each pet
for pet in pets:
    print(f"Animal: {pet['animal']}, Owner: {pet['owner']}")

# print the definitions of 6 programming words
programming_words = {
    'function': 'A block of code that performs a specific task.',
    'list': 'A collection of items that can be ordered and changeable.',
    'tuple': 'A collection of items that are ordered and unchangeable.',
    'dictionary': 'A collection of key-value pairs.',
    'condition': 'A statement that is either true or false.',
    'loop': 'A statement that repeats a block of code.'
}

for word, definition in programming_words.items():
    print(f"{word}: {definition}")
    print()