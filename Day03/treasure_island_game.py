print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Greet the user
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Prompt the user to select one of the two options
turn = input('You\'re at a cross roads. ' # Break up the prompt into multiple lines for the user's convenience
             'Which turn do you take? (Type "left" or "right"):\n').lower()  # Convert the input into lowercase

# Based on the user's selection, either end the game or move the user one step closer to the treasure
if turn == "left":
    next_step = input('You\'ve entered an enchanted forest. ' 
                      'There\'s a lake ahead of you. '
                      'Do you swim across or walk around the lake? (Type "swim" or "walk"):\n').lower()
    if next_step == "swim":
        last_step = input('You\'ve successfully swum across the lake and come across a small hut. '
                          'Which entrance do you choose? (Type "front door", "side window" or "chimney"):\n').lower()
        if last_step == "front door":
            print("You run into a wicked witch and get cursed. Game Over.")
        elif last_step == "chimney":
            print("You get stuck in the chimney. Game over.")
        elif last_step == "side window":
            print("You sneak past the wicked witch and find the hidden treasure. You win!")
        else:
            print("You knock over an oil lamp and the hut goes up in flames. Game Over.")
    else:
        print("You get attacked by a grizzly bear. Game Over.")
else:
    print("You step into quicksand and get pulled under. Game Over.")