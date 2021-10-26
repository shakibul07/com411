x = int(input("what level of brightness is required "))
print("Adjusting....")
for count in range(2,x
        +1,2):
    print(f"Beeps brightness level: {count * '*'}")
    print(f"Bops brightness level: {count * '*'}")

print("Adjusting complete...")