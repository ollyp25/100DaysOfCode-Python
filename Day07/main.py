# Import the modules
import random
import hangman_art
import hangman_words

# Greet the user
print(hangman_art.logo)

# Initialise the number of lives, select the word for the user to guess
lives = 6
chosen_word = random.choice(hangman_words.word_list)

# Print the placeholder
placeholder = "_" * len(chosen_word) # Each "_" represents a single letter of the word
print(placeholder)

display = ["_"] * len(chosen_word)
guessed = [] # Keep track of the guessed letters

# Prompt the user to guess a letter
# Continue prompting the user until the word is guessed OR lives have run out
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print(f"You've already guessed {guess}.")
    elif guess in chosen_word:
        guessed.append(guess)
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
    else:
        lives -= 1 # Deduct a life if the guess is incorrect
        print(f"**************** WRONG GUESS // {lives} LIVES LEFT ****************")

    print("".join(display))
    print(hangman_art.stages[lives])

# If the loop breaks because the lives have run out
if lives == 0:
    print(f"The word you were trying to guess was {chosen_word}.")
    # Let the user know that they've lost
    print("******************** YOU LOST ********************")

# Else, if the word was guessed correctly
else:
    print(hangman_art.stages[lives])
    print(chosen_word)
    # Let the user know that they've won
    print("********************* YOU WIN *********************")