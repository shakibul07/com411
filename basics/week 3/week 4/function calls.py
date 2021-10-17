def display_box(word):
    num_dashes = 4  + len (word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("_"* num_dashes)

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")

def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitations = int(input())

    for repetitations in range(repetitations):
        if (repetitations % 2 == 0):
            print(display_lower_case(word))

        else:
            print(display_upper_case((word)))

def run():
    print("please enter a word : ")
    word = input()

    print("What would you like to with this word? ")
    print("1] Display in a box")
    print("[2] Display lower case")
    print("[3] display upper case")
    print("[4] display mirrored")
    print("[5] diplay repeated ")
    print("[6] Quit")

    response = int(input())

    if response == 1 :
        display_box(word)
    elif response == 2:
        display_lower_case(word)
    elif response == 3:
        display_upper_case(word)
    elif response == 4:
        display_mirrored(word)
    elif response == 5:
        display_repeated(word)
    else:
        print("Unknown")

run()