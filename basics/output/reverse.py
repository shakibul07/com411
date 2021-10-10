print("What phrase do you see ?")
phrase = input()

#identify markings
print("\n reversing...")
print("The phrase is ", end="")

for position in range(len(phrase) -1,-1,-1):
    print(phrase[position], end="")
