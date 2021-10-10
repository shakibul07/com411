# ask user live cable for avoid
print("How many live cables must i avoid ? ")
avoidcables = int(input())
lives = 1

while lives < avoidcables:
    print(f"avoiding...Done! {lives} live cables avoided.")
    lives = lives + 1

print("All cables have been avoided. ")

# in question input 3 but printing 1 2 3
# in here input 3 lives 0 but printing 0 1 2
# in here input 3 lives 1 but printing 1 2 only
