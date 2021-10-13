print("Program started! ")
char= int(input("Please enter an Ascii code: "))

value = chr(char)

if char >= 32 and char <= 126:
    print(f"the ascii value {char} and ascii charector is: {value}")

else:
    print("the charector is not identify")

print(" program ended ! ")
