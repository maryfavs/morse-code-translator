#You will use what you've learnt to create a text-based (command line) program that takes any String input and converts
# it into Morse Code.
import sys

print("=" * 36)
print("Welcome to my very own Morse Coder")
print("=" * 36)

morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/",
    "0" : "−−−−−",
    "1" : "·−−−−",
    "2" : "··−−−",
    "3" : "···−−",
    "4" : "····−",
    "5" : "·····",
    "6" : "−····",
    "7" : "−−···",
    "8" : "−−−··",
    "9" : "−−−−·"
    }

should_continue = True

while should_continue:
    text = input("Enter a text: ").upper()

    new_text = ""

    for letter in text:
        if letter not in morse_code:
            print(f"{letter} is not in the dictionary")
            print("Only letters A-Z, numbers 0 - 9 and spaces are allowed")
            sys.exit()
        else:
            new_text += morse_code[letter] + " "
    print(f"Translation: {new_text}")

    retry = input("Would you like to go again? (y/n)").lower()
    if retry == "n":
        should_continue = False

    else:
        should_continue = True

print("You have come to the end of the program!")

