import art

print(art.logo)

# Predefine the list of alphabet letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the Caesar function
def caesar(original_text, shift_amount, encode_or_decode):
    #Initialise an empty output string
    output_text = ""

    # If the user selected decryption, change the direction of the shift
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        # Skip over non alphabetic symbols
        if not letter.isalpha():
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            # Make sure the index wraps around the alphabet list
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    # Return the result
    return f"Here is the {encode_or_decode}d result: {output_text}"

# Keep prompting the user for input unless asked to stop
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the encryption function and pass the user input as arguments and print the result
    result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    print(result)

    # Ask the user if they'd like to encrypt more messages
    restart = input("Would you like to encode/decode another phrase?(Type 'yes' or 'no'): ").lower()
    if restart != "yes":
        break


