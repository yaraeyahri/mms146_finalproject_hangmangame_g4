import random

def load_categories(HangmanRandomWordGenerator.txt);
  with open(HangmanRandomWordGenerator.txt, 'r') as file:
    lines = file.read().strip().split('\n')

  categories = {}
  current_category = None

  for line in lines:
    if line.strip(): # Ignore empty lines
      if not current_category = # It's not a category
        current_category = line.strip()
        categories[current_category] = []
    else: # It's a word

categories[current_category].append(line.strip())
  current_caategory = None
return categories

def select_random_word(categories):
  # Choose a random category
  category = random.choice(list(categories.keys()))

# Choose a random word from that category
word = random.choice(categories[category])

return category, word

# Example usage
HangmanRandomWordGenerator.txt = 'categories.txt'
categories = load_categories(HangmanRandomWordGenerator.txt)
category, word = select_random_word(categories)

print(f"Category: {category}")
print(f"Word: {word}")
