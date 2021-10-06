#ask user type of cover book

print(" What is the type of the book cover? ( hard / soft) ? ")
book = input()

#soft cover result
if book == "soft":

    #ask it is perfect bound
    print("is the book is perfect bound ? (yes / no) ")
    perfect_bound = input()

    if perfect_bound == "yes":
        print(" Soft cover , perfect bound books are very populer! ")
    else :
        print("Soft covers with coils or stitches are great for short cooks ")

elif book == "hard":
    print("Books with hard covers can be more expensive! ")

else:
    print(" Invalid !!!, try again . ")
