
# Day 10 - Functions with Outputs

### Concepts Learned: 
- Python functions with outputs
- Using functions to reduce redundant code

## Project of the Day - Calculator
- [Calculator](Day10/main.py)

### How It Works

1. User Input: The program asks the user to enter two numbers and choose an arithmetic operation (addition, subtraction, multiplication, or division).
2. Calculation: Based on the chosen operation, the program performs the corresponding arithmetic calculation using the two input numbers.
3. Result: The program displays the result of the calculation in the format: number1 operation number2 = result.
4. Additional Calculations: After displaying the result, the user is prompted to either perform another calculation using the current result or start over with new numbers. This process repeats until the user decides to exit.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

Enter number 1: 75
Choose operation (type +, -, * or /): -
Enter number 2: 12
75 - 12 = 63
Type 'y' to perform another calculation, 'n' to start over: y
Choose operation (type +, -, * or /): *
Enter number 2: 10
63 * 10 = 630
Type 'y' to perform another calculation, 'n' to start over: n
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.