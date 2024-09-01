import random
def load_categories(filename):

    categories = {}
    current_categories = None
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line: # Skip empty lines
                continue
            if line.startswith('#'): # Ignore empty lines
                current_category = line[1:].strip()
                categories[current_category] = []
            else: # It's a word
                if current_category is not None:
                    categories[current_category].append(line)
            
    return categories
def select_random_word(categories):
    # Choose a random category
    category = random.choice(list(categories.keys()))
    # Choose a random word from the category
    word = random.choice(categories[category])
    return category, word

# Example usage
filename = 'HangmanRandomWordGenerator.txt'
categories = load_categories(filename)
category, word = select_random_word(categories)

print(f"Category: {category}")
print(f"Word: {word}")
