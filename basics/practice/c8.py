level = int(input("what level of brightness is required ? "))

print("adjusting brightness...")


for count in range(2,level+1,2):
    print(f"beeps brightness level : {'*' * count}")
    print(f"bops brightness level : {'*' * count}")
    count+=1

print("adujustment complete...")