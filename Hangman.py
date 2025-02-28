import random

# ASCII Art Stages
stages = [
    r"""
      +---+
          |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      O   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      O   |
      |   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      O   |
     /|   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      O   |
     /|\  |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      O   |
     /|\  |
     /    |
          |
          |
    =========
    """,
    r"""
      +---+
      O   |
     /|\  |
     / \  |
          |
          |
    =========
    """
]

# Word Categories
easy_list = [
    'apple', 'banana', 'grape', 'mango', 'peach', 'lemon', 'orange',
    'chair', 'table', 'pencil', 'school', 'clock', 'mirror', 'plant',
    'ocean', 'river', 'cloud', 'beach', 'island', 'sunset', 'forest'
]
medium_list = [
    'elephant', 'giraffe', 'dolphin', 'kangaroo', 'penguin', 'crocodile',
    'diamond', 'amethyst', 'emerald', 'sapphire', 'crystal', 'obsidian',
    'laptop', 'keyboard', 'monitor', 'printer', 'charger', 'backpack',
    'pyramid', 'treasure', 'journey', 'lantern', 'airplane', 'glacier'
]
hard_list = [
    'xylophone', 'quarantine', 'psychology', 'philosophy', 'encyclopedia',
    'architecture', 'chrysanthemum', 'parliament', 'rhinoceros', 'telescope',
    'zoology', 'vortex', 'hologram', 'knapsack', 'whimsical', 'algorithm',
    'pneumonia', 'microscope', 'camouflage', 'ambiguous', 'labyrinth'
]
super_hard_list = [
    'antidisestablishmentarianism', 'floccinaucinihilipilification',
    'pseudopseudohypoparathyroidism', 'hippopotomonstrosesquipedaliophobia',
    'supercalifragilisticexpialidocious', 'sesquipedalian',
    'uncharacteristically', 'misconception', 'idiosyncrasy', 'onomatopoeia'
]

# Ask user for difficulty level
print("Choose a difficulty level: ")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("4. Super Hard")

difficulty_choice = input("Enter the number of your choice: ")

if difficulty_choice == "1":
    word_list = easy_list
elif difficulty_choice == "2":
    word_list = medium_list
elif difficulty_choice == "3":
    word_list = hard_list
elif difficulty_choice == "4":
    word_list = super_hard_list
else:
    print("Invalid choice! Defaulting to Easy mode.")
    word_list = easy_list

# Pick a random word from the selected difficulty
choose = random.choice(word_list)

# Initialize game variables
lives = 6
blank = '-' * len(choose)
print(blank)

game_over = False
corrected_letters = []
display = blank

while not game_over:
    user = input('Guess a letter: ').lower()
    
    # Check if letter was already guessed
    if user in corrected_letters or user in display:
        print(f"You already guessed '{user}'. Try another letter.")
        continue
    
    # Update the display
    new_display = ""
    found = False
    
    for letter in choose:
        if letter == user:
            new_display += user
            found = True
        elif letter in display:
            new_display += letter
        else:
            new_display += "-"
    
    # Deduct lives if the letter is incorrect
    if not found:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
    
    # Update the displayed word and guessed letters
    display = new_display
    corrected_letters.append(user)
    
    print(display)
    print(stages[lives])

    # Win condition
    if '-' not in display:
        print("🎉 You win! 🎉")
        game_over = True

    # Lose condition
    if lives == 0:
        print(f"😢 You lose! The word was '{choose}'.")
        game_over = True
