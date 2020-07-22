from IMC_symbols import morse_code
import time


def text2morse_trans(text):
    text_ = text.split(" ")
    morse_trans = []
    for word in text_:

        for char in word:
            morse_char = morse_code[char.upper()]
            morse_trans.append(morse_char)
        morse_trans.append(" ")

    return morse_trans


def print_morse(morse_trans_list):
    for m in morse_code:
        if m == " ":
            print("/", end=" ")
        print(m, end="  ")


text = "hey there"  # input()
morse_code = text2morse_trans(text)
print_morse(morse_code)
