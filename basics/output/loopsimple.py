#ask the user for how many to show
print("How many mountains should i display ? ")
mountains = int(input())

i = 1
sum = 0
print("Displaying..... ")
while i <= mountains:
    i += 1
    print("          __          ")
    print("         /  \_        ")
    print("        /^   \        ")
    print("       /   ^  \_      ")
    print("     _/ ^  ^    ^\    ")
    print("   _/   ^  ^      ^ \   ")
    print(" /  ^    ^           \  ")
    sum += i
print("Done!  ")