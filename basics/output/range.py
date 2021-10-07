print("What level of brightness is required ? ")
level = int(input())


print("Adujusting brightness... ")

for brightness in range(2, level + 1, 2):
    print(f"Beeps brightness level :{'*' * brightness}")
    print(f"bops brightness level : {'*' * brightness}")
