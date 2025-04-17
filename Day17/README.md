
# Day 17 - OOP and Custom Classes

### Concepts Learned: 

On Day 17 I learned how to create custom classes from scratch using Object-Oriented Programming. I applied this by building a True/False quiz game, where I used my own classes to manage questions, user interaction, and scoring. The project reinforced how to structure and use objects effectively in a real-world program.

## Project of the Day
- [Quiz Project](Day17/main.py)

### How It Works

The program uses OOP to build a quiz game. It converts raw question data into Question objects and stores them in a question_bank. The QuizBrain class manages quiz logic, presenting each question and checking answers. The game continues until all questions are answered, then displays the user’s final score.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
Q.1: The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution. (True or False?): False
You got it right!
The correct answer was: False.
Your current score is: 1/1


Q.2: Pointers were not used in the original C programming language; they were added later on in C++. (True or False?): True
That's wrong.
The correct answer was: False.
Your current score is: 1/2


Q.3: Linux was first created as an alternative to Windows XP. (True or False?): True
That's wrong.
The correct answer was: False.
Your current score is: 1/3


Q.4: The Windows 7 operating system has six main editions. (True or False?): False
That's wrong.
The correct answer was: True.
Your current score is: 1/4


Q.5: &quot;HTML&quot; stands for Hypertext Markup Language. (True or False?): False
That's wrong.
The correct answer was: True.
Your current score is: 1/5


Q.6: The Windows ME operating system was released in the year 2000. (True or False?): True
You got it right!
The correct answer was: True.
Your current score is: 2/6


Q.7: Linus Torvalds created Linux and Git. (True or False?): False
That's wrong.
The correct answer was: True.
Your current score is: 2/7


Q.8: The logo for Snapchat is a Bell. (True or False?): False
You got it right!
The correct answer was: False.
Your current score is: 3/8


Q.9: RAM stands for Random Access Memory. (True or False?): True
You got it right!
The correct answer was: True.
Your current score is: 4/9


Q.10: The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot; (True or False?): True
You got it right!
The correct answer was: True.
Your current score is: 5/10


You've completed the quiz!
Your final score was: 5/10
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program, for example, by adding more advanced features like input validation, dynamic tip percentages, or a graphical user interface (GUI).
