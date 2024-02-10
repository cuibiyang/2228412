def morse_translator(text):
    # Morse code dictionary
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..'}
    
    # Convert the text to uppercase for case insensitivity
    text = text.upper()
    
    morse_result = []  # List to store Morse code for each character
    for char in text:
        if char.isalpha():  # Check if character is alphabetic
            morse_result.append(morse_code[char])
        elif char == ' ':  # Space between words
            morse_result.append('/')
    
    # Join Morse codes for characters and words
    return ' '.join(morse_result)

# Example usage:
text_to_translate = "Hello World"
print(morse_translator(text_to_translate))  # Output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
