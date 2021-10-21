print("How many live cables should i avoid? ")
cables = int(input())

cable = 1
while cable <= cables:
    print(f"Avoiding... done! {cable} live cables avoided")
    cable += 1

print(" All live cables have been avoided . ")
