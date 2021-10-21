print("program started ! ")
charecter = str(input("Please enter a standard charecter:  "))

if len(charecter) == 1 :
    value = ord(charecter)
    print(f"the ascii code for {charecter} is {value}...")
else:
    print("something invaild ...try again!!!")

print("Program ended !!!!")