
# Day 26 - List & Dictionary Comprehensions

### Concepts Learned: 

Today we explored one of Python’s powerful features—list and dictionary comprehensions—which help simplify and shorten our code when working with collections.

By the end of the lesson, we built a console program that converts any word into the NATO phonetic alphabet. 

The project gave great hands-on practice with comprehensions and working with CSV data in Python.

## Project of the Day
- [Nato Alphabet](Day26/main.py)

### How It Works

This interactive program converts each letter of a word into its corresponding NATO phonetic alphabet code. It begins by loading a CSV file containing the phonetic alphabet into a dictionary. Each letter is paired with its phonetic code, which is then used to look up the code for each letter in the user-inputted word. The program prompts the user to enter a word, converts each letter to uppercase, and then translates the word into a list of phonetic codes. The list of phonetic codes is displayed as the final output.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
Enter a word: John
['Juliet', 'Oscar', 'Hotel', 'November']
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.
