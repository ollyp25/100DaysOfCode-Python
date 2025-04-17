
# Day 14 - Higher or Lower

### Concepts Learned: 
Day 14 was dedicated to practicing everything I'd learned up until that point by completing a capstone project.

## Project of the Day 
- [Higher or Lower](Day14/main.py)

### How It Works

1. Display Logo: The game begins by displaying a logo using ASCII art from the art module.
2. Random Selection: Two random items are selected from a dataset (data), each representing a person or entity with a follower count.
3. Comparison Setup: The player is shown details about "Object A" and "Object B", including their name, description, and country.
4. Player Guess: The player is asked to guess which object has more followers by typing "A" or "B".
5. Checking the Guess: The program compares the follower counts:
- If the player is correct, their score increases by one, and they receive positive feedback.
- If the player is incorrect, the game ends and the final score is displayed.
6. Next Round: If the player guessed correctly:
- "Object B" becomes the new "Object A".
- A new "Object B" is randomly selected from the remaining data.
7. This loop continues until the player makes a wrong guess.
8. Data Management: Each round, the previously compared object is removed from the dataset to avoid repetition.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Priyanka Chopra Jonas, Actress and musician, from India.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Compare B: FC Barcelona, Football club, from Spain.
Who has more followers? Type 'A' or 'B': B
You're right! Current score: 1
Compare A: FC Barcelona, Football club, from Spain.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Compare B: Shawn Mendes, Musician, from Canada.
Who has more followers? Type 'A' or 'B': B
Sorry, that's wrong. Final score: 1
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program, for example, by adding more advanced features like input validation, dynamic tip percentages, or a graphical user interface (GUI).
