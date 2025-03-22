import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")

# Global constants
easy_lives = 10
hard_lives = 5

def play_round(number, tries):
    '''Play a round until all lives have run out and compare user's guess against computer's number.'''
    lives = tries
    while lives > 0:
        guess = int(input("Take a guess: "))
        if guess < number:
            lives -= 1
            if lives >= 1:
                print("Too low. Try again.")
                print(f"You have {lives} lives remaining.")
        elif guess > number:
            lives -= 1
            if lives >= 1:
                print("Too high. Try again.")
                print(f"You have {lives} lives remaining.")
        else:
            print(f"You got it! The number I was thinking of was {number}.")
            return

    print("Uh-oh! You've used up all your lives.")
    print(f"The number I was thinking of was {number}. You lose :(")

def game():
    '''Main function that loops until user doesn't want to play anymore'''
    game_over = False
    while not game_over:
        number = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100.")
        level = input("Choose a level of difficulty (type 'easy' or 'hard'): ").lower()

        if level == "easy":
            play_round(number, 10)
        elif level == "hard":
            play_round(number, 5)

        another_round = input("Would you like to play another round? (Type 'y' or 'n'): ")
        if another_round == "n":
            game_over = True


if __name__ == "__main__":
    game()