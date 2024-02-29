morse_code = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    # Symbols
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...',
    ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

reversed_morse_code = {value: key for key, value in morse_code.items()}


def enlish_to_moores():
    result = ""
    can_not_convert = []
    user_text = input("Enter Your English Text\n  />> ").upper()
    for char in user_text:
        if char == " ":
            result += "   "
        elif char not in morse_code:
            can_not_convert.append(char)
            result += char + " "
        else:
            result += morse_code[char] + " "
    if len(can_not_convert) != 0:
        print(f"Charecters that can not be converted\n  />> {can_not_convert}")
    print(f"Moores Code Representation\n  />> {result}")
    return


def moores_to_english():
    result = ""
    user_text = input("Enter Your Moores Text\n  />> ").split(' ')
    for r in range(len(user_text)):
        try:
            if user_text[r] == "" and user_text[r + 1] == "" and user_text[r + 2] == "":
                result += " "
        except IndexError:
            # result = result
            pass
        if user_text[r] not in reversed_morse_code:
            result += user_text[r]
        else:
            result += reversed_morse_code[user_text[r]]
    print(f"English Representation uppercase\n  />> {result}")
    print(f"English Representation lowercase\n  />> {result.lower()}")
    return

# enlish_to_moores()
moores_to_english()
