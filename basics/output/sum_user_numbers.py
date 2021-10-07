print("how many numbers should i sum up ? ")
numbers = int(input())

i = 0
sum= 0

while i < numbers :
    i += 1
    ask =input("Please enter number " + str(i) +" of " + str(numbers) +"  : ")
    print(ask)
    sum += int(ask)

print("The answer is " + str(sum))