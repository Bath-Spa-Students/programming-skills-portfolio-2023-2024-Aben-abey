# Create a glossary dictionary with programming terms and their meanings
glossary = {
    'variable': 'An identifier related with a capacity area, holding information either known or obscure alluded to as a value.',
    'function': 'A named segment of a program that carries out a specific assignment, handling input information to create output.',
    'loop': 'A programming structure that emphasizes through a grouping of enlightening until a particular condition is met.',
    'condition': 'A articulation or expression that assesses to genuine or wrong, essential for making choices inside a program.',
    'dictionary': 'A information structure in Python that stores key-value sets, guaranteeing each key is interesting for proficient information mapping.',
    'list': 'An requested collection of things competent of containing different information sorts, permitting for modification.',
    'tuple': 'An unchanging collection of things regularly utilized for holding settled arrangements of data.',
    'set': 'A collection of unmistakable components without a characterized arrange, useful for mathematical operations.',
    'module': 'A Python record typifying code, encouraging code organization and reuse over different projects.',
    'class': 'A format for making objects having particular traits and behaviors.'
}

# Print each word and its meaning with a newline between each pair using a loop
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")
    print()  # Insert a blank line after each word-meaning pair
