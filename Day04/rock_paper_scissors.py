import random

# Predefine ASCII graphics
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Prompt the user to go first
player = int(input("Make your choice: Type 0 for Rock, 1 for Paper, or 2 for Scissors "))

# Computer's turn
computer = random.randint(0, 2)

# Select a winner based on the rules of the game and print the result
if player == 0:
    if computer == 0:
        print(rock)
        print(f"Computer chose:\n{rock}")
        print("It's a draw!")
    elif computer == 1:
        print(rock)
        print(f"Computer chose:\n{paper}")
        print("You lose :(")
    else:
        print(rock)
        print(f"Computer chose:\n{scissors}")
        print("You win :)")
elif player == 1:
    if computer == 0:
        print(paper)
        print(f"Computer chose:\n{rock}")
        print("You win :)")
    elif computer == 1:
        print(paper)
        print(f"Computer chose:\n{paper}")
        print("It's a draw")
    else:
        print(paper)
        print(f"Computer chose:\n{scissors}")
        print("You lose :(")
else:
    if computer == 0:
        print(scissors)
        print(f"Computer chose:\n{rock}")
        print("You lose :(")
    elif computer == 1:
        print(scissors)
        print(f"Computer chose:\n{paper}")
        print("You win :)")
    else:
        print(scissors)
        print(f"Computer chose:\n{scissors}")
        print("It's a draw!")