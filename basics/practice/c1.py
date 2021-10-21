print("Please enter the first whole number!! ")
fnum = int(input())
print("Please enter the secound whole number !!!")
snum = int(input())
print("Please enter the third whole number !!!")
tnum = int(input())

even = 0
odd = 0

if fnum % 2 == 0 :
    even += 1
else :
    odd += 1

if snum % 2 == 0 :
    even += 1
else :
    odd += 1

if tnum % 2 == 0 :
    even += 1
else :
    odd += 1

print(f"There were {even} even and {odd} odd numbers ")