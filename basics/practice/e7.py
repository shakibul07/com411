user = int(input("Please enter a number? "))
count = 1
factorial = 1

while count <= user:
    factorial = count * factorial
    count += 1
print(f"the factorial is {factorial}")