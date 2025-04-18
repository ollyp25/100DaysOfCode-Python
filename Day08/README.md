
# Day 8 - Function Parameters & Caesar Cipher

### Concepts Learned:

- Python Functions with Inputs
- Positional vs Keyword Arguments

## Project of the Day - Caesar Cipher

This program allows you to encode or decode messages using the Caesar Cipher method where each letter in the original text is shifted a certain number of places in the alphabet.

- [Caesar Cipher in Python](Day08/main.py)

### How It Works

1. Prompt user to type encode to encrypt a message or decode to decrypt a message.
2. Prompt the user for the text that they want to encode or decode.
3. Ask the user how many positions each letter in their message should be shifted.
4. After printing the result, ask the user if they'd like to encode or decode another message. If yes, the program will continue to run; else, the program will stop.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello, world!
Type the shift number:
3
Here is the encoded result: khoor, zruog!
Would you like to encode/decode another phrase?(Type 'yes' or 'no'): yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor, zruog!
Type the shift number:
3
Here is the decoded result: hello, world!
Would you like to encode/decode another phrase?(Type 'yes' or 'no'): no
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.