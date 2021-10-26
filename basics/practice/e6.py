num = int(input("how many numbers should i sum up ?"))
count = 1
total = 0
while count <= num:
    print(f"Please enter number {count} of {num}")
    user_in= int(input())
    total += int(user_in)
    count+= 1
print(f"the answer is {total}")