import art
import random
from game_data import data

# Print the logo art
print(art.logo)

def game():
    score = 0 # Initiate the score
    game_over = False

    # Select random subjects from the data dict
    object_a, object_b = random.sample(data, 2)

    while not game_over:
        # Print two subjects for comparison
        print(f"Compare A: {object_a['name']}, {object_a['description']}, from {object_a['country']}.")
        print(art.vs)
        print(f"Compare B: {object_b['name']}, {object_b['description']}, from {object_b['country']}.")

        # Prompt user for selection
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Check if the answer is correct or wrong and adjust the score accordingly
        if guess == "A" and object_a["follower_count"] > object_b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
        elif guess == "B" and object_a["follower_count"] < object_b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")

        # If answer is wrong, stop the game and print the user's final score
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

        # Remove already used subjects from the dict and re-assign subjects for comparison
        data.remove(object_a)
        object_a = object_b
        object_b = random.choice([item for item in data if item != object_a])

if __name__ == "__main__":
    game()