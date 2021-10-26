charecter = input("please enter a standard charector:").lower()

if len(charecter) == 1:
    value = ord(charecter)
    print(f"The ascii code for {charecter} is {value}")
else:
    print("Error")
print("Program ended.......")