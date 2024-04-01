# Create a glossary dictionary with programming terms and their meanings
glossary = {
    'variable': 'An identifier linked to a storage location, holding known or unknown data known as a value.',
    'function': 'A named program section executing a specific task, processing input to produce output.',
    'loop': 'A programming pattern repeating instructions until a specific condition is satisfied.',
    'condition': 'A statement or expression producing true or false results, crucial for program decision-making.',
    'dictionary': 'A Python data structure storing unique key-value pairs for efficient value mapping.'
}

# Print each word and its meaning with a newline between each pair
for word, meaning in glossary.items():
    print(f"{word}:")
    print(meaning)
    print()  # Insert a blank line after each word-meaning pair
