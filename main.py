# Define the dictionary for Morse code translation
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', 
    ')': '-.--.-'
}

# Function to encrypt the input string into Morse code
def encrypt(string):
    cipher = ''  # Initialize an empty string to store the Morse code
    for letter in string:  # Loop through each character in the input string
        cipher += MORSE_CODE[letter] + ' '  # Convert letter to Morse code and add a space
    return cipher  # Return the Morse code string

# Main function to run the program
def main():
    print("Welcome to the Morse Code Encrypt")  # Print welcome message
    string = str(input("Say your word to Morse Code Converter: "))  # Get user input and convert to string
    result = encrypt(string.upper())  # Convert the string to uppercase and encrypt it into Morse code
    print(f"Here is your Morse Code: {result}")  # Print the resulting Morse code

# Call the main function to execute the program
main()
