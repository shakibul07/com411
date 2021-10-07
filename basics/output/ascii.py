#ask user bar of charge
print("How many bars should be charged? ")
numberofbars = int(input())
bars = 0

while bars <= numberofbars:
    j = 1
    while j <= bars:
         print( "*", end ="")
         j += 1
    print()
    bars +=1

print("The battery is fully charged. ")


