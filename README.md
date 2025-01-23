# Morse Code Converter

This is a simple Python script that converts a given string (letters, digits, and some special characters) into Morse code.

## Features
- Converts alphabets (A-Z), numbers (0-9), and some special characters (., ?, /, -, etc.) into their corresponding Morse code.
- Takes user input through the console and outputs the corresponding Morse code.

## Requirements
- Python 3.x

## How to Run
1. Clone the repository or download the `morse_code_converter.py` file.
2. Open a terminal or command prompt.
3. Navigate to the folder where the script is saved.
4. Run the script by typing:
    ```bash
    python morse_code_converter.py
    ```

5. Input a word or sentence when prompted. The script will convert it to Morse code and print the result.

## Example


## Code Overview
- The `MORSE_CODE` dictionary contains the mapping for each letter, number, and some special characters to their corresponding Morse code representation.
- The `encrypt` function takes the input string, looks up the corresponding Morse code for each character, and concatenates them with a space between each code.
- The `main` function handles user input, calls the `encrypt` function, and prints the Morse code result.

## Contributing
Feel free to fork the project, submit issues, or open pull requests to contribute.

## License
This project is open source and available under the MIT License.
