bars = int(input("How many bars should be charged?  "))
charged = 1
while charged <= bars:
    print(f"Charging : {charged * '|'}")
    charged += 1

print("The battery id fully charged")