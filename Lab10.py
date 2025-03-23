
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

#Function for removing unwanted characters
def filter_sentence(sentence):
    sentence = sentence.lower()
    return ''.join([char for char in sentence if char in morse_code_dict or char == ' '])

#Function to add characters to a list and dictate spaces
def add_to_morse_list(sentence):
    morse_list = []
    words = sentence.split()
    
    for i, word in enumerate(words):
        for j, char in enumerate(word):
            morse_code = morse_code_dict[char]
            for symbol in morse_code:
                morse_list.append(symbol)
            if j < len(word) - 1:  # Space between characters
                morse_list.append('   ')
        if i < len(words) - 1:  # Space between words
            morse_list.append('       ')
    return morse_list


sentence = input("Write a sentence: ")
filtered_sentence = filter_sentence(sentence)
morse_translation = add_to_morse_list(filtered_sentence)
print(" ".join(morse_translation))  


