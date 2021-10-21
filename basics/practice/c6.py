phrase = str(input("WHat pharase do you see ?  "))

for position in range (len (phrase)-1, -1,-1):
    print(phrase[position],end="")