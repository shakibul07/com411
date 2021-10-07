Numlist = []
Even_count= 0
odd_count = 0

for i in range (1, 5):
    value = int(input("please enter %d user number : " %i))
    Numlist.append(value)

for j in range(4):
    if (Numlist[j] % 2 == 0):
        Even_count =Even_count+ 1
    else:
        odd_count = odd_count + 1

print(" There were " + str ( Even_count) + "  even and " + str(odd_count) + "  odd numbers. ")