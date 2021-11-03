print("Please enter a number? ")
number = int(input())

fac = 0
i = 1
x = 1
while i <= number:
    fac = x * i
    x *= i
    i = i + 1
print(fac)

