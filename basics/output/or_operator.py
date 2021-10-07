#ask what type of advanture
print("Enter type of adventure? ('scary'/'short'/'safe'/'long') ")
typead = input()

if (typead == "scary") or (typead == "short"):
    print ( " Entering the dark forest")

elif (typead ==  "safe") or (typead == "long"):
    print ( " Taking the safe route! ")

else:
    print(" Not sure which route to take. ")