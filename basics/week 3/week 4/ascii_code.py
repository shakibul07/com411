print("Program Started!")
stand=input("please enter a standard charactor : ")
if len(stand) == 1 :
    value = ord(stand)
    print(f"The ASCII code for {stand} is {value}")
else:
    print("Error ! too many charectors. Please input one charector at once .")

print("Program ended !  ")