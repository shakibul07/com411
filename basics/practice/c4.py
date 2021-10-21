insum = int(input("How many numbers should i sum up"))
num = 0
sum = 0


while num < insum :
    num += 1
    print(f"please enter number {num} of {insum} ..")
    numb = int(input())
    sum += numb

print(sum)