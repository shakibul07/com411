print("How many rows should i have? ")
row = int(input())
print("How many columns should I have? ")
columns = int(input())
print("Here I go: ")



for count in range(0,row,1):
    for number in range(0,columns,1):
        print(":-)",end="")
    print()