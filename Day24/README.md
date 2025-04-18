
# Day 24 - Files, Folders & Automating Tasks

### Concepts Learned: 

Today was all about working with the local file system and understanding how directories operate in Python. We started by upgrading our Snake game to save the high score between plays—by reading from and writing to a file. Now, even after the game ends, we can track our best score over time!

After that, we shifted gears to a real-world automation project. Imagine needing to send personalized letters to a list of people—like birthday invites or thank-you notes. Instead of manually editing each one, we used Python to:
- Read a list of names from a file 📄
- Replace a placeholder (like [name]) in a letter template
- Generate a custom letter for each person automatically

It’s a small but powerful way Python can help automate repetitive tasks.

## Project of the Day
- [Turtle Crossing Game](Day23/main.py)

### How It Works

1. This program automates the process of creating personalized letters from a single template. Here's how it works:
2. Read Names: It starts by opening the invited_names.txt file, which contains a list of names. Each name is read into a list.
3. Read Template Letter: It then opens a starting letter template (starting_letter.txt) that contains a placeholder ([name]) where each name should go.
4. Personalize & Save:
- For each name, it removes any extra whitespace.
- Replaces [name] in the template with the actual name.
- Writes the personalized letter to a new .txt file in the Output/ReadyToSend folder, naming it letter_for_<name>.txt.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.
