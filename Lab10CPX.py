import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.2
cp.pixels.fill((0, 0, 0))
cp.pixels.show()

morse_code_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
    "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----"
}

def filter_sentence(sentence):
    sentence = sentence.lower()
    return ''.join([char for char in sentence if char in morse_code_dict or char == ' '])

def add_to_morse_list(sentence):
    morse_list = []
    words = sentence.split()
    
    for i, word in enumerate(words):
        for j, char in enumerate(word):
            morse_code = morse_code_dict[char]
            for symbol in morse_code:
                morse_list.append(symbol)
            if j < len(word) - 1:  # Space between characters within a word
                morse_list.append('   ')
        if i < len(words) - 1:  # Space between words
            morse_list.append('       ')
    return morse_list

def morse_display(morse_list, unit_length):
    for i, symbol in enumerate(morse_list):

        if symbol == '.':
            cp.pixels.fill((255, 255, 255))  # White for dot
            cp.pixels.show()
            time.sleep(unit_length)
        elif symbol == '-':
            cp.pixels.fill((255, 0, 0))  # Red for dash
            cp.pixels.show()
            time.sleep(3 * unit_length)
        elif symbol == '   ':  # Space between characters
            cp.pixels.fill((0, 0, 0))
            cp.pixels.show()
            time.sleep(3 * unit_length)
        elif symbol == '       ':  # Space between words
            cp.pixels.fill((0, 0, 0))
            cp.pixels.show()
            time.sleep(7 * unit_length)
        else:
            print(f"Unknown symbol: '{symbol}'")  
        

        cp.pixels.fill((0, 0, 0))
        cp.pixels.show()
        time.sleep(unit_length)

while True:
    try:
        unit_length = float(input("Enter the length of a unit (between 0 and 1 second): "))
        if 0 < unit_length <= 1:
            break
        print("Please enter a value between 0 and 1")
    except ValueError:
        print("Please enter a valid number")

sentence = input("Write a sentence: ")
filtered_sentence = filter_sentence(sentence)
morse_translation = add_to_morse_list(filtered_sentence)
morse_display(morse_translation, unit_length)
