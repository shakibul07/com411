print("Program started....")
x = int(input("Please enter an ascii number: "))

if x>= 32 and x<=126:
    print(f"The charecter repreasented by the Ascii Code {x} is {chr(x)}")
else:
    print("number out of range try between 32 - 126")
print("Programme ended....")