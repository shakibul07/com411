print("How far are we from the cave ?  ")
farfrom = int(input())

i = 1
sum = farfrom

while i <= farfrom:
    i += 1
    print("{} steps remaining. ".format(sum))
    sum -= 1